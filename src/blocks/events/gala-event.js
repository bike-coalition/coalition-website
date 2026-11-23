/*
  Golden Gear Gala event page section: plays the muted reel on a loop and runs its pause button,
  and makes "Get tickets" scroll down to the Givebutter ticket widget on the same page.
  The video only starts if the visitor's device doesn't ask for less motion; otherwise it shows the poster
  with a play button. It also pauses while scrolled out of view, to save battery and data.
  Without this script the video shows its poster and stays still, and "Get tickets" opens the Givebutter page.
*/
(function(){
 function reel(root){
  var v=root.querySelector('video'), b=root.querySelector('.bc-gev__pause');
  if(!v||!b) return;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var wanted=!reduce; // what the visitor last chose
  function label(){
   var playing=!v.paused;
   b.textContent=playing?'❚❚':'▶';
   b.setAttribute('aria-label',playing?'Pause the gala video':'Play the gala video');
  }
  function play(){ var p=v.play(); if(p&&p.catch) p.catch(function(){ label(); }); }
  v.addEventListener('play',label); v.addEventListener('pause',label);
  b.addEventListener('click',function(){ wanted=v.paused; if(wanted) play(); else v.pause(); });
  b.hidden=false;
  if('IntersectionObserver' in window){
   new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ if(wanted) play(); } else if(!v.paused){ v.pause(); } }); },{threshold:0.2}).observe(v);
  } else if(wanted){ play(); }
  label();
 }
 function tickets(root){
  var a=root.querySelector('[data-bc-gev-tickets]'); if(!a) return;
  a.addEventListener('click',function(e){
   var w=document.querySelector('givebutter-widget'); if(!w) return; // no widget on the page: follow the link to Givebutter
   var t=w.closest('.sqs-block')||w;
   e.preventDefault();
   var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
   var header=document.querySelector('.header'); t.style.scrollMarginTop=((header&&header.offsetHeight)||0)+24+'px';
   if(!t.hasAttribute('tabindex')) t.setAttribute('tabindex','-1');
   t.scrollIntoView({behavior:reduce?'auto':'smooth',block:'start'});
   try { t.focus({preventScroll:true}); } catch(err){ t.focus(); }
  });
 }
 function init(root){
  if(root.dataset.ready) return; root.dataset.ready='1';
  reel(root); tickets(root);
 }
 [].forEach.call(document.querySelectorAll('[data-bc-gev]'),init);
})();
