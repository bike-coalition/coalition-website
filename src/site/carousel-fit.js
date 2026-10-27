/*
  Every Squarespace summary carousel (blog, shop, events): fit the row of cards to the cards on screen.
  Squarespace makes the row as tall as its tallest card, even one several slides away, which leaves a
  big gap under the cards you can see. This sets the row's height to the tallest card in view and
  updates it as the carousel slides, the window resizes or images load. Does nothing in the editor.
  Loaded site-wide from Code Injection > Header (src/site/header-injection.html).
*/
(function(){
  if(document.body.classList.contains('sqs-edit-mode')) return;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function init(list){
    if(list.dataset.bcFit) return; list.dataset.bcFit='1';
    var items=[].slice.call(list.children);
    if(!items.length) return;
    if(!reduce) list.style.transition='transform 0.4s, height 0.4s';

    function fit(){
      // Squarespace slides the row with translateX(-N%), a percentage of the row's own width
      var m=/translateX\((-?[\d.]+)%\)/.exec(list.style.transform||'');
      var left=m ? -parseFloat(m[1])/100*list.offsetWidth : 0, right=left+list.offsetWidth, h=0, mb=0;
      items.forEach(function(it){
        var mid=it.offsetLeft+it.offsetWidth/2;
        // The cards' bottom margin is part of the row Squarespace builds (the last card has none, so use the largest)
        mb=Math.max(mb,parseFloat(getComputedStyle(it).marginBottom)||0);
        if(mid>=left && mid<=right && it.offsetHeight>h) h=it.offsetHeight;
      });
      h=h&&h+mb;
      if(h && list.style.height!==h+'px') list.style.height=h+'px';
    }

    new MutationObserver(fit).observe(list,{attributes:true,attributeFilter:['style']});
    if(window.ResizeObserver){ var ro=new ResizeObserver(fit); items.forEach(function(it){ro.observe(it);}); ro.observe(list.parentElement); }
    else window.addEventListener('resize',fit);
    fit();
  }

  function run(){ document.querySelectorAll('.summary-block-wrapper.sqs-gallery-design-carousel .summary-item-list').forEach(init); }
  run();
  window.addEventListener('load',run);
})();
