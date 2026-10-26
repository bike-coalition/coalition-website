/*
  Board Candidates page: candidate picker. Builds the roster buttons, shows one candidate at a time
  with previous and next buttons, and adds each candidate's photo from the data-photo attribute in the markup.
  Runs on every [data-bc-board] block on the page; does nothing where there is none.
  Without it, every candidate shows, stacked, with initials instead of photos.
*/
(function(){
 function init(root){
  if(root.dataset.ready) return; root.dataset.ready=1;
  var cands=[].slice.call(root.querySelectorAll('.bc-board__cand')), ro=root.querySelector('.bc-board__roster'), btns=[], cur=0;
  root.classList.add('is-ready');
  cands.forEach(function(c,i){
   var n=c.getAttribute('data-name'), photo=c.getAttribute('data-photo'); c.querySelector('.bc-board__count').textContent='Candidate '+(i+1)+' of '+cands.length;
   if(photo){var im=new Image();im.alt='Portrait of '+n;im.src=photo;c.querySelector('.bc-board__photo').appendChild(im);}
   var b=document.createElement('button');b.type='button';b.className='bc-board__pick'+(c.classList.contains('is-dark')?' is-dark':'');b.style.setProperty('--t',c.style.getPropertyValue('--t'));
   b.innerHTML='<b></b><span></span>';b.firstChild.textContent=n;b.lastChild.textContent=c.getAttribute('data-short');
   b.onclick=function(){show(i)};ro.appendChild(b);btns.push(b);
   var nav=document.createElement('div');nav.className='bc-board__nav';var pn=cands[(i+cands.length-1)%cands.length].getAttribute('data-name'),nn=cands[(i+1)%cands.length].getAttribute('data-name');nav.innerHTML='<button type="button" class="bc-board__prev"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M12 5l-7 7 7 7"/></svg></button><button type="button" class="bc-board__next"><span></span><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg></button>';nav.firstChild.setAttribute('aria-label','Previous candidate: '+pn);nav.lastChild.firstChild.textContent='Next:  '+nn;
   nav.firstChild.onclick=function(){show((i+cands.length-1)%cands.length)};nav.lastChild.onclick=function(){show((i+1)%cands.length)};
   c.lastElementChild.appendChild(nav);
  });
  function show(i){cur=i;cands.forEach(function(c,k){c.classList.toggle('is-active',k===i)});btns.forEach(function(b,k){b.setAttribute('aria-pressed',k===i)});}
  show(0);
 }
 [].forEach.call(document.querySelectorAll('[data-bc-board]'),init);
})();
