"""
Make the inline "guard" style for a Code block from its stylesheet.

Keeps only the size and position rules (display, widths, margins, padding, flex and grid,
fonts, borders): no colors, hovers or motion. Paste the output inside the <style> at the
top of the block's .html file, so the Squarespace editor measures the block at its real
size before the stylesheet loads (docs/jsdelivr-plan.md, step 1 lessons).

Usage: python3 tools/make-guard.py src/blocks/classes/find-your-class.css
"""
import re,sys
LAYOUT=re.compile(r'^(display|position|inset|top|left|right|bottom|width|height|min-width|min-height|max-width|max-height|margin(-[\w-]+)?|padding(-[\w-]+)?|flex(-[\w-]+)?|grid(-[\w-]+)?|gap|row-gap|column-gap|overflow(-[xy])?|aspect-ratio|box-sizing|font-size|line-height|font|font-family|font-weight|letter-spacing|text-transform|align-[\w-]+|justify-[\w-]+|place-items|white-space|border|border-width|border-top|border-bottom|border-left|border-right|object-fit|object-position|list-style|--[\w-]+)$')
def strip_comments(s): return re.sub(r'/\*.*?\*/','',s,flags=re.S)
def guard_rules(css):
    out=[]
    def rules(block):
        res=[]; i=0
        while i<len(block):
            j=block.find('{',i)
            if j<0: break
            sel=block[i:j].strip()
            if sel.startswith('@media'):
                depth=1;k=j+1
                while depth: depth+= {'{':1,'}':-1}.get(block[k],0); k+=1
                inner=rules(block[j+1:k-1])
                if inner: res.append(sel+'{'+''.join(inner)+'}')
                i=k; continue
            if sel.startswith('@'):
                depth=1;k=j+1
                while depth: depth+= {'{':1,'}':-1}.get(block[k],0); k+=1
                i=k; continue
            k=block.find('}',j); decls=block[j+1:k]; i=k+1
            sels=[x.strip() for x in sel.split(',') if not re.search(r':(hover|focus|focus-visible|disabled|active)|::-webkit|::marker',x)]
            if not sels: continue
            keep=[]
            for d in re.split(r';(?![^(]*\))',decls):
                d=d.strip()
                if not d or ':' not in d: continue
                p=d.split(':',1)[0].strip()
                if LAYOUT.match(p): keep.append(re.sub(r'\s*:\s*',':',d,count=1))
            if keep: res.append(','.join(sels)+'{'+';'.join(keep)+'}')
        return res
    return ''.join(rules(re.sub(r'\s+',' ',strip_comments(css))))
if __name__=='__main__': print(guard_rules(open(sys.argv[1]).read()))
