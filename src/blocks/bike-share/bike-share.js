/*
  Bike Share page: the three pickers (Unlock, Ride, Dock steps; the five route stops; the five funding pillars).
  Each [data-picker] row of buttons shows one panel from the matching [data-panels] group at a time.
  The buttons carry aria-pressed; each points to its panel with aria-controls.
  Without this script every panel shows, stacked, so nothing is lost. Runs on every [data-bc-bshare] block; does nothing where there is none.
*/
(function(){
 function setup(root,name){
  var row=root.querySelector('[data-picker="'+name+'"]'), group=root.querySelector('[data-panels="'+name+'"]');
  if(!row||!group) return;
  var tabs=[].slice.call(row.querySelectorAll('button[aria-controls]'));
  function show(i){
   tabs.forEach(function(t,k){
    t.setAttribute('aria-pressed',k===i?'true':'false');
    var p=document.getElementById(t.getAttribute('aria-controls'));
    if(p){ if(k===i) p.removeAttribute('hidden'); else p.setAttribute('hidden',''); }
   });
  }
  tabs.forEach(function(t,i){ t.addEventListener('click',function(){ show(i); }); });
  show(0);
 }
 /* A link like /bike-share#support jumps before the petition embed and photos have loaded; they then grow the page above the target
    and push it out of view. Keep the target in place while the block settles (up to 8 seconds), and stop as soon as the visitor scrolls. */
 function holdAnchor(root){
  var id=decodeURIComponent(location.hash.slice(1)); if(!id) return;
  var t=document.getElementById(id); if(!t||!root.contains(t)) return;
  var done=false, timer, evs=['wheel','touchstart','keydown','mousedown'];
  function go(){ if(!done) t.scrollIntoView({block:'start',behavior:'instant'}); }
  function stop(){ done=true; mo.disconnect(); evs.forEach(function(e){ removeEventListener(e,stop,true); }); }
  var mo=new MutationObserver(function(){ clearTimeout(timer); timer=setTimeout(go,120); });
  mo.observe(root,{childList:true,subtree:true,attributes:true,attributeFilter:['style','class','hidden']});
  evs.forEach(function(e){ addEventListener(e,stop,{capture:true,passive:true}); });
  addEventListener('load',function(){ go(); setTimeout(go,600); });
  setTimeout(function(){ go(); stop(); },8000);
  go();
 }
 function init(root){
  if(root.dataset.ready) return; root.dataset.ready='1';
  ['step','stop','pillar'].forEach(function(n){ setup(root,n); });
  root.classList.add('is-ready');
  holdAnchor(root);
 }
 [].forEach.call(document.querySelectorAll('[data-bc-bshare]'),init);
})();
