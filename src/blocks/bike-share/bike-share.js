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
 function init(root){
  if(root.dataset.ready) return; root.dataset.ready='1';
  ['step','stop','pillar'].forEach(function(n){ setup(root,n); });
  root.classList.add('is-ready');
 }
 [].forEach.call(document.querySelectorAll('[data-bc-bshare]'),init);
})();
