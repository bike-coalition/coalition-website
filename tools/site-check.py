#!/usr/bin/env python3
"""
Read-only check of the live site: broken links, image alt text, and page weight.

Reads the sitemap, loads every page, then:
- checks every link on it (internal and external), following redirects,
- flags images with missing or empty alt text that aren't marked decorative,
- records HTML size and the number and size of images and scripts.

It only sends GET and HEAD requests, identifies itself with its own user agent, skips
anything robots.txt disallows, waits at least 0.5s between requests to any one host
(about 2 per second), and checks each URL once per run. Writes a dated Markdown report.

Exit code: 1 if any internal link is broken, 2 if the sitemap can't be read, else 0.

Python 3.9+ standard library only. Usage:
  python3 tools/site-check.py                      # full run, report in docs/reports/
  python3 tools/site-check.py --limit 10 --out /tmp  # quick trial on 10 pages
"""
import argparse, datetime, gzip, os, re, ssl, statistics, sys, threading, time
import urllib.error, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser

SITE = 'https://sdbikecoalition.org'
SITE_HOSTS = {'sdbikecoalition.org', 'www.sdbikecoalition.org'}
UA = 'SDBikeCoalitionSiteCheck/1.0 (+https://github.com/bike-coalition/coalition-website; read-only weekly check)'
TIMEOUT = 20
# External sites that answer these to automated checks usually work fine in a browser.
BLOCKED = {401, 403, 429, 999}
# Squarespace writes an "add to Google Calendar" link on every event page; there is nothing to fix in them.
GENERATED = re.compile(r'^https?://(www\.)?google\.com/calendar/(event|render)\?.*action=TEMPLATE', re.I)
SKIP_SCHEMES = ('mailto:', 'tel:', 'sms:', 'javascript:', 'data:', 'blob:', 'about:')
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}
FILENAME_ALT = re.compile(r'\.(jpe?g|png|gif|webp|heic|svg|avif)\s*$|^(img|dsc|pxl|untitled)[ _-]?\d', re.I)
IMAGE_WIDTH = 1500  # srcset width used for the image weight estimate (a typical laptop)


# ===== fetching =====

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k): return None  # we follow redirects ourselves, one rate-limited hop at a time

def ssl_context():
    ctx = ssl.create_default_context()
    if not ctx.get_ca_certs() and os.path.exists('/etc/ssl/cert.pem'):
        ctx.load_verify_locations('/etc/ssl/cert.pem')  # python.org builds on macOS ship without CA certificates
    return ctx

OPENER = urllib.request.build_opener(NoRedirect, urllib.request.HTTPSHandler(context=ssl_context()))

class Result:
    def __init__(self, url):
        self.url, self.status, self.final, self.chain, self.error = url, None, url, [], None
        self.headers, self.body, self.size = {}, b'', None
    @property
    def ok(self): return self.error is None and self.status is not None and self.status < 400

class Fetcher:
    def __init__(self, interval):
        self.interval, self.locks, self.last, self.guard = interval, defaultdict(threading.Lock), {}, threading.Lock()
        self.cache, self.cache_lock, self.count = {}, threading.Lock(), 0

    def _wait(self, host):
        with self.guard: lock = self.locks[host]
        lock.acquire()
        gap = self.interval - (time.monotonic() - self.last.get(host, 0))
        if gap > 0: time.sleep(gap)
        return lock

    def _once(self, url, method, read):
        host = urllib.parse.urlsplit(url).hostname or ''
        lock = self._wait(host)
        try:
            req = urllib.request.Request(url, method=method, headers={'User-Agent': UA, 'Accept': 'text/html,application/xhtml+xml,*/*;q=0.8'})
            try: resp = OPENER.open(req, timeout=TIMEOUT)
            except urllib.error.HTTPError as e: resp = e
            body = b''
            if method == 'GET' and read is not None and resp.fp is not None:
                body = resp.read() if read == -1 else resp.read(read)
            resp.close()
            return resp.status, dict(resp.headers.items()), body
        finally:
            self.last[host] = time.monotonic(); lock.release()
            with self.guard: self.count += 1

    def fetch(self, url, method='GET', read=-1):
        """Follow up to 10 redirects. One retry on a network error, 429 or 5xx."""
        r = Result(url); cur = url
        for _ in range(10):
            for attempt in (1, 2):
                try:
                    status, headers, body = self._once(cur, method, read); err = None
                except Exception as e:
                    status, headers, body, err = None, {}, b'', short_error(e)
                if (err or status == 429 or (status or 0) >= 500) and attempt == 1: time.sleep(3); continue
                break
            if err: r.error = err; r.final = cur; return r
            if status in (301, 302, 303, 307, 308) and headers.get('Location'):
                nxt = urllib.parse.urljoin(cur, headers['Location'])
                r.chain.append((status, nxt)); cur = nxt
                if status == 303: method = 'GET'
                continue
            r.status, r.final, r.headers = status, cur, {k.lower(): v for k, v in headers.items()}
            if r.headers.get('content-encoding') == 'gzip':
                try: body = gzip.decompress(body)
                except OSError: pass
            r.body = body
            return r
        r.error = 'too many redirects'; return r

    def cached(self, key, fn):
        with self.cache_lock:
            if key in self.cache: return self.cache[key]
        res = fn()
        with self.cache_lock: self.cache.setdefault(key, res)
        return self.cache[key]

    def check_link(self, url):
        """HEAD first; GET if HEAD fails (some servers refuse or mishandle HEAD)."""
        def go():
            r = self.fetch(url, 'HEAD')
            if not r.ok: r = self.fetch(url, 'GET', read=65536)
            return r
        return self.cached(('link', url), go)

    def asset_size(self, url):
        """Bytes as served without compression. HEAD Content-Length, or download it."""
        def go():
            r = self.fetch(url, 'HEAD')
            if r.ok and r.headers.get('content-length', '').isdigit():
                r.size = int(r.headers['content-length']); return r
            r = self.fetch(url, 'GET')
            if r.ok: r.size = len(r.body)
            r.body = b''
            return r
        return self.cached(('size', url), go)

def short_error(e):
    if isinstance(e, urllib.error.URLError): e = e.reason
    return (type(e).__name__ + ': ' + str(e))[:120]

def clean(url):
    """Drop the #fragment and make the URL safe to request."""
    url = urllib.parse.urldefrag(url.strip())[0]
    return urllib.parse.quote(url, safe=":/?#[]@!$&'()*+,;=%~")


# ===== robots.txt (the "User-agent: *" group, with * and $ wildcards) =====

def robots_rules(text):
    groups, agents, rules, last = [], [], [], None
    for line in text.splitlines():
        line = line.split('#', 1)[0].strip()
        if ':' not in line: continue
        k, v = [x.strip() for x in line.split(':', 1)]; k = k.lower()
        if k == 'user-agent':
            if last == 'rule': groups.append((agents, rules)); agents, rules = [], []
            agents.append(v.lower()); last = 'agent'
        elif k in ('allow', 'disallow'):
            if v: rules.append((k == 'allow', v))
            last = 'rule'
    groups.append((agents, rules))
    return [r for a, rs in groups if '*' in a for r in rs]

def robots_allowed(rules, url):
    p = urllib.parse.urlsplit(url); path = (p.path or '/') + ('?' + p.query if p.query else '')
    best = (-1, True)
    for allow, pat in rules:
        rx = re.escape(pat).replace(r'\*', '.*')
        if rx.endswith(r'\$'): rx = rx[:-2] + '$'
        if re.match(rx, path) and (len(pat) > best[0] or (len(pat) == best[0] and allow)): best = (len(pat), allow)
    return best[1]


# ===== page parsing =====

class PageParser(HTMLParser):
    def __init__(self, base):
        super().__init__(convert_charrefs=True)
        self.base, self.stack = base, []
        self.links, self.images, self.scripts = [], [], []
        self.inline_scripts, self.inline_bytes, self.in_script = 0, 0, False

    def handle_starttag(self, tag, attrs):
        a = {}
        for k, v in attrs: a.setdefault(k, v or '')  # browsers use the first copy of a repeated attribute
        decorative_parent = any(d for _, d in self.stack)
        hidden_here = a.get('aria-hidden') == 'true' or 'section-background' in a.get('class', '')
        if tag not in VOID: self.stack.append((tag, hidden_here))
        in_noscript = any(t == 'noscript' for t, _ in self.stack)
        if tag == 'a' and a.get('href'):
            href = a['href'].strip()
            if href and not href.startswith('#') and not href.lower().startswith(SKIP_SCHEMES):
                url = urllib.parse.urljoin(self.base, href)
                if not GENERATED.match(url): self.links.append(url)
        elif tag == 'img' and not in_noscript:
            src = a.get('src') or a.get('data-src') or ''
            if src.startswith('data:') or '/memberAccountAvatars/' in src: return  # blog author avatars come from Squarespace, not us
            decorative = (decorative_parent or hidden_here or a.get('role') in ('presentation', 'none')
                          or (a.get('width') == '1' and a.get('height') == '1'))
            alt = a.get('alt')
            issue = None
            if alt is None: issue = 'missing'
            elif not alt.strip(): issue = 'empty'
            elif FILENAME_ALT.search(alt): issue = 'file name'
            if issue in ('missing', 'empty') and decorative: issue = None
            self.images.append({'src': urllib.parse.urljoin(self.base, src) if src else '',
                                'weigh': image_weight_url(a, self.base), 'alt': alt, 'issue': issue})
        elif tag == 'script':
            if a.get('src'): self.scripts.append(urllib.parse.urljoin(self.base, a['src']))
            else: self.in_script = True; self.inline_scripts += 1

    def handle_endtag(self, tag):
        if tag == 'script': self.in_script = False
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag: del self.stack[i:]; break

    def handle_data(self, data):
        if self.in_script: self.inline_bytes += len(data.encode('utf-8'))

def image_weight_url(a, base):
    """The file a laptop browser would likely load: the srcset entry nearest IMAGE_WIDTH."""
    cands = []
    for part in (a.get('srcset') or '').split(','):
        bits = part.split()
        if len(bits) == 2 and bits[1].endswith('w') and bits[1][:-1].isdigit(): cands.append((int(bits[1][:-1]), bits[0]))
    if cands:
        cands.sort(); pick = next((u for w, u in cands if w >= IMAGE_WIDTH), cands[-1][1])
        return urllib.parse.urljoin(base, pick)
    src = a.get('src') or a.get('data-src') or ''
    if not src: return ''
    url = urllib.parse.urljoin(base, src)
    if 'squarespace-cdn.com' in url and 'format=' not in url:
        url += ('&' if '?' in url else '?') + f'format={IMAGE_WIDTH}w'
    return url


# ===== sitemap =====

def read_sitemap(f, url, seen=None):
    seen = seen if seen is not None else set()
    r = f.fetch(url)
    if not r.ok: log(f'Could not read the sitemap {url}: {r.error or r.status}'); sys.exit(2)
    root = ET.fromstring(r.body); ns = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
    if root.tag == ns + 'sitemapindex':
        out = []
        for loc in root.iter(ns + 'loc'):
            if loc.text and loc.text not in seen: seen.add(loc.text); out += read_sitemap(f, loc.text.strip(), seen)
        return out
    return [u.findtext(ns + 'loc').strip() for u in root.iter(ns + 'url') if u.findtext(ns + 'loc')]


# ===== run =====

def is_internal(url): return (urllib.parse.urlsplit(url).hostname or '').lower() in SITE_HOSTS

def log(msg): print(msg, file=sys.stderr, flush=True)

def run(args):
    f = Fetcher(1 / args.rate)
    started = datetime.datetime.now(TZ)
    robots = f.fetch(SITE + '/robots.txt')
    rules = robots_rules(robots.body.decode('utf-8', 'replace')) if robots.ok else []
    pages = list(dict.fromkeys(clean(u) for u in read_sitemap(f, args.sitemap)))
    if args.limit: pages = pages[:args.limit]
    log(f'{len(pages)} pages from the sitemap')

    data, found_on = {}, defaultdict(set)
    for i, url in enumerate(pages, 1):
        if not robots_allowed(rules, url): data[url] = {'skipped': True}; continue
        r = f.fetch(url)
        d = {'status': r.status, 'error': r.error, 'final': r.final, 'html': len(r.body)}
        if r.ok and 'html' in r.headers.get('content-type', ''):
            p = PageParser(r.final)
            try: p.feed(r.body.decode('utf-8', 'replace')); p.close()
            except Exception as e: d['parse_error'] = short_error(e)
            d.update(links=p.links, images=p.images, scripts=list(dict.fromkeys(p.scripts)),
                     inline_scripts=p.inline_scripts, inline_bytes=p.inline_bytes)
            for link in p.links: found_on[clean(link)].add(url)
        r.body = b''
        f.cache[('link', url)] = r  # a link to this page is answered by this fetch
        data[url] = d
        if i % 25 == 0: log(f'  loaded {i}/{len(pages)} pages')

    links = sorted(found_on)
    skipped = [u for u in links if is_internal(u) and not robots_allowed(rules, u)]
    to_check = [u for u in links if u not in skipped and not (args.no_external and not is_internal(u))]
    assets = sorted({x for d in data.values() for x in [i['weigh'] for i in d.get('images', [])] + d.get('scripts', []) if x})
    log(f'checking {len(to_check)} links and sizing {len(assets)} images and scripts')
    jobs = [(f.check_link, u) for u in to_check] + [(f.asset_size, u) for u in assets]
    with ThreadPoolExecutor(max_workers=8) as pool:
        for n, _ in enumerate(pool.map(lambda j: j[0](j[1]), jobs), 1):
            if n % 200 == 0: log(f'  {n}/{len(jobs)} done')
    link_res = {u: f.cache[('link', u)] for u in to_check}
    size_res = {u: f.cache[('size', u)] for u in assets}
    log(f'{f.count} requests in {int(time.monotonic() - T0)}s')
    return dict(started=started, pages=pages, data=data, found_on=found_on, link_res=link_res,
                size_res=size_res, skipped=skipped, requests=f.count, args=args)


# ===== report =====

def kb(n): return f'{n / 1024:,.0f} KB' if n < 1024 * 1024 else f'{n / 1048576:,.1f} MB'

def path(url):
    p = urllib.parse.urlsplit(url)
    if (p.hostname or '') in SITE_HOSTS: return (p.path or '/') + ('?' + p.query if p.query else '')
    return url

def plural(n, word): return f'{n} {word}' + ('' if n == 1 else 's')

def md(s): return str(s).replace('|', '\\|').replace('\n', ' ')

def pages_cell(urls, n=5):
    urls = sorted(urls, key=lambda u: (len(u), u))
    s = ', '.join(f'`{md(path(u))}`' for u in urls[:n])
    return s + (f' and {len(urls) - n} more' if len(urls) > n else '')

def describe(r):
    if r.error: return r.error
    return f'{r.status}'

def weights(R):
    rows = []
    for url, d in R['data'].items():
        if 'images' not in d: continue
        imgs = list(dict.fromkeys(i['weigh'] for i in d['images'] if i['weigh']))
        isz = [R['size_res'][u].size for u in imgs]; ssz = [R['size_res'][u].size for u in d['scripts']]
        img_b = sum(s or 0 for s in isz); scr_b = sum(s or 0 for s in ssz)
        rows.append(dict(url=url, html=d['html'], imgs=len(imgs), img_b=img_b, scripts=len(d['scripts']), scr_b=scr_b,
                         inline=d['inline_scripts'], inline_b=d['inline_bytes'], unknown=sum(s is None for s in isz + ssz),
                         total=d['html'] + img_b + scr_b))
    return sorted(rows, key=lambda r: -r['total'])

def report(R):
    data, found_on, link_res = R['data'], R['found_on'], R['link_res']
    broken_int, broken_ext, blocked, redirects = [], [], [], []
    for u, r in link_res.items():
        internal = is_internal(u)
        if r.ok:
            if internal and r.chain:
                downgrade = any(n.startswith('http://') for _, n in r.chain)
                if downgrade or path(r.final).rstrip('/') != path(u).rstrip('/'): redirects.append((u, r, downgrade))
        elif internal: broken_int.append((u, r))
        elif r.status in BLOCKED or 'CERTIFICATE_VERIFY_FAILED' in (r.error or ''): blocked.append((u, r))
        else: broken_ext.append((u, r))
    failed_pages = [(u, d) for u, d in data.items() if d.get('error') or (d.get('status') or 0) >= 400]
    alt_issues = defaultdict(set)  # (image, problem, alt) -> pages, so a footer image shows up once
    for u, d in data.items():
        for i in d.get('images', []):
            if i['issue']: alt_issues[(i['src'], i['issue'], i['alt'])].add(u)
    n_alt = {k: sum(key[1] == k for key in alt_issues) for k in ('missing', 'empty', 'file name')}
    alt_pages = set().union(*[v for k, v in alt_issues.items() if k[1] != 'file name']) if alt_issues else set()
    loaded = [u for u, d in data.items() if 'images' in d]
    everywhere = sum(len(v) == len(loaded) > 1 for k, v in alt_issues.items() if k[1] != 'file name')
    W = weights(R)
    med = lambda k: statistics.median(r[k] for r in W) if W else 0
    when = R['started']
    L = []
    L += [f'# Site check, {when:%B} {when.day}, {when:%Y}', '',
          f'Automated read-only check of {SITE} by `tools/site-check.py`, started {when:%Y-%m-%d %H:%M %Z}. '
          f'{len(R["pages"])} pages from the sitemap, {len(link_res)} unique links checked, {R["requests"]} requests in all.', '',
          '## Summary', '', '| Check | Result |', '| --- | --- |',
          f'| Pages checked | {len(W)} loaded, {len(failed_pages)} failed |',
          f'| **Broken internal links** | **{len(broken_int)}** (on {plural(len(set().union(*[found_on[u] for u, _ in broken_int])) if broken_int else 0, "page")}) |',
          f'| Broken external links | {len(broken_ext)} |',
          f'| External links the other site would not let us check | {len(blocked)} (check these by hand) |',
          f'| Internal links that redirect somewhere else | {len(redirects)} ({sum(d for *_, d in redirects)} drop to plain http) |',
          f'| Images with no alt text | {n_alt["missing"] + n_alt["empty"]} different images, on {len(alt_pages)} pages'
          + (f' ({everywhere} of them are on every page, so likely in the header or footer)' if everywhere else '') + ' |',
          f'| Images whose alt text is a file name | {n_alt["file name"]} different images |',
          f'| Typical page (median) | {kb(med("html"))} HTML, {med("imgs"):.0f} images ({kb(med("img_b"))}), {med("scripts"):.0f} scripts ({kb(med("scr_b"))}) |']
    if W: L.append(f'| Heaviest page | `{path(W[0]["url"])}`, {kb(W[0]["total"])} |')
    if R['skipped']: L.append(f'| Internal links skipped (robots.txt asks crawlers not to load them) | {len(R["skipped"])} |')
    if R['args'].no_external: L.append('| External links | not checked this run (--no-external) |')
    L += ['', 'Broken internal links make this check fail. Everything else is for review.', '']

    if failed_pages:
        L += ['## Pages in the sitemap that failed to load', '', '| Page | Result |', '| --- | --- |']
        L += [f'| `{md(path(u))}` | {md(d.get("error") or d.get("status"))} |' for u, d in failed_pages] + ['']
    L += ['## Broken internal links', '']
    if broken_int:
        L += ['| Link | Result | Found on |', '| --- | --- | --- |']
        L += [f'| `{md(path(u))}` | {md(describe(r))} | {pages_cell(found_on[u])} |' for u, r in sorted(broken_int)]
    else: L.append('None.')
    L += ['', '## Broken external links', '']
    if broken_ext:
        L += ['| Link | Result | Found on |', '| --- | --- | --- |']
        L += [f'| {md(u)} | {md(describe(r))} | {pages_cell(found_on[u])} |' for u, r in sorted(broken_ext)]
    else: L.append('None.' if not R['args'].no_external else 'Not checked this run.')
    L += ['', '## External links to check by hand', '',
          'These sites answered 401, 403, 429 or 999, which usually means they turn away automated checks, or their security '
          'certificate could not be verified (often a server setup gap that browsers work around). They may work fine in a browser.', '']
    if blocked:
        L += ['| Link | Result | Found on |', '| --- | --- | --- |']
        L += [f'| {md(u)} | {r.status or "certificate not verified"} | {pages_cell(found_on[u], 3)} |' for u, r in sorted(blocked)]
    else: L.append('None.')
    L += ['', '## Internal links that redirect', '', 'Not broken, but worth pointing straight at the final page.', '']
    if redirects:
        L += ['| Link | Ends at | Found on |', '| --- | --- | --- |']
        L += [f'| `{md(path(u))}` | {md(r.final)}{" **(plain http)**" if d else ""} | {pages_cell(found_on[u], 3)} |'
              for u, r, d in sorted(redirects, key=lambda x: (not x[2], x[0]))]
    else: L.append('None.')
    L += ['', '## Image alt text', '',
          'Images with no alt attribute, an empty one, or a file name for alt text. Images inside section backgrounds, '
          'or marked `aria-hidden` or `role="presentation"`, count as decorative and are left out.', '']
    if alt_issues:
        L += ['| Image | Problem | Alt text now | Found on |', '| --- | --- | --- | --- |']
        for (src, issue, alt), on in sorted(alt_issues.items(), key=lambda x: (-len(x[1]), x[0][1], x[0][0])):
            name = urllib.parse.unquote(src.rsplit('/', 1)[-1].split('?')[0])[:60] or '(no src)'
            L.append(f'| [{md(name)}]({src}) | {issue} | {md(alt or "")} | {pages_cell(on, 3)} |')
    else: L.append('None.')
    L += ['', '## Page weight', '',
          f'Sizes are as served before compression. Image weight counts each image at about {IMAGE_WIDTH}px wide (the '
          f'srcset entry nearest that), so it overstates pages full of small thumbnails, like blog lists; phones load less. "Inline" is script written into the page HTML, already counted in the HTML size. '
          'Sorted heaviest first.', '',
          '| Page | Total | HTML | Images | Scripts | Inline scripts |', '| --- | --: | --: | --: | --: | --: |']
    for w in W:
        unk = f' ({w["unknown"]} unsized)' if w['unknown'] else ''
        L.append(f'| `{md(path(w["url"]))}` | {kb(w["total"])}{unk} | {kb(w["html"])} | {w["imgs"]}, {kb(w["img_b"])} | '
                 f'{w["scripts"]}, {kb(w["scr_b"])} | {w["inline"]}, {kb(w["inline_b"])} |')
    if R['skipped']:
        L += ['', '## Skipped internal links', '', 'robots.txt asks crawlers not to load these, so the check leaves them alone.', '']
        L += [f'- `{md(path(u))}`' for u in R['skipped'][:10]]
        if len(R['skipped']) > 10: L.append(f'- and {len(R["skipped"]) - 10} more (mostly calendar `?format=ical` links)')
    return '\n'.join(L) + '\n', len(broken_int)


try:
    from zoneinfo import ZoneInfo
    TZ = ZoneInfo('America/Los_Angeles')
except Exception:
    TZ = datetime.timezone.utc
T0 = time.monotonic()

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--sitemap', default=SITE + '/sitemap.xml')
    ap.add_argument('--out', default='docs/reports', help='folder for the report (default docs/reports)')
    ap.add_argument('--rate', type=float, default=2.0, help='most requests per second to any one host (default 2)')
    ap.add_argument('--limit', type=int, default=0, help='check only the first N pages (for trial runs)')
    ap.add_argument('--no-external', action='store_true', help="don't check links to other sites")
    args = ap.parse_args()
    args.rate = min(args.rate, 2.0)
    R = run(args)
    text, n_broken = report(R)
    os.makedirs(args.out, exist_ok=True)
    out = os.path.join(args.out, f'site-check-{R["started"]:%Y-%m-%d}.md')
    with open(out, 'w') as fh: fh.write(text)
    log(f'report: {out}')
    if n_broken: log(f'{n_broken} broken internal links'); sys.exit(1)
