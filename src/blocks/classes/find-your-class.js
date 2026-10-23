/*
  Classes page: "Find your class" carousel arrows, pager and keyboard.
  Runs on every [data-bc-classes] block on the page; does nothing where there is none.
*/
(function(){
 function init(root){
 if(root.dataset.ready) return; root.dataset.ready=1;
  var track=root.querySelector('.bc-classes__track'), slides=[].slice.call(root.querySelectorAll('.bc-classes__slide')), pager=root.querySelector('[data-pager]'),
      prev=root.querySelector('[data-prev]'), next=root.querySelector('[data-next]'), n=slides.length, dots=[], labels=['City Cycling','Smart Cycling','Bike Rodeo','Assemblies & More'];
  function pos(i){return slides[i].offsetLeft-slides[0].offsetLeft}
  function go(i){i=Math.max(0,Math.min(n-1,i));track.scrollTo({left:pos(i),behavior:'smooth'})}
  function current(){var max=track.scrollWidth-track.clientWidth;if(track.scrollLeft>=max-4)return n-1;var best=0,d=1e9;for(var i=0;i<n;i++){var x=Math.abs(track.scrollLeft-pos(i));if(x<d){d=x;best=i}}return best}
  function sync(){var c=current();dots.forEach(function(b,j){b.setAttribute('aria-current',j===c?'true':'false')});prev.disabled=track.scrollLeft<=4;next.disabled=track.scrollLeft>=track.scrollWidth-track.clientWidth-4}
  for(var k=0;k<n;k++){(function(k){var b=document.createElement('button');b.type='button';b.setAttribute('aria-label','Show '+labels[k]);b.addEventListener('click',function(){go(k)});pager.appendChild(b);dots.push(b)})(k)}
  prev.addEventListener('click',function(){go(current()-1)});
  next.addEventListener('click',function(){go(current()+1)});
  track.addEventListener('keydown',function(e){if(e.key==='ArrowLeft'){e.preventDefault();go(current()-1)}if(e.key==='ArrowRight'){e.preventDefault();go(current()+1)}});
  var raf;track.addEventListener('scroll',function(){cancelAnimationFrame(raf);raf=requestAnimationFrame(sync)},{passive:true});
  window.addEventListener('resize',sync);
  sync();
 }
 [].forEach.call(document.querySelectorAll('[data-bc-classes]'),init);
})();
