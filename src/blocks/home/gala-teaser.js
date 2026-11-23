/*
  Homepage Golden Gear Gala teaser: plays the muted reel on a loop and runs its pause button.
  The video only starts if the visitor's device doesn't ask for less motion; otherwise it shows the poster
  with a play button. It also pauses while scrolled out of view, to save battery and data.
  Without this script the video shows its poster (the title card) and stays still.
*/
(function(){
 function init(root){
  if(root.dataset.ready) return; root.dataset.ready='1';
  var v=root.querySelector('video'), b=root.querySelector('.bc-gala__pause');
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
 [].forEach.call(document.querySelectorAll('[data-bc-gala]'),init);
})();
