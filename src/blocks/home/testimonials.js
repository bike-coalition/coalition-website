/*
  Homepage: "What people are saying" testimonials carousel.
  Runs on every .bc-quotes block on the page; does nothing where there is none.
*/
(function(){
  function init(root){
    if(root.dataset.ready) return; root.dataset.ready='1';
    var slides=[].slice.call(root.querySelectorAll('.bc-quotes__slide'));
    var dotsWrap=root.querySelector('.bc-quotes__dots'), dots=[], i=0, timer=null;
    var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    slides.forEach(function(s,n){
      s.setAttribute('role','group'); s.setAttribute('aria-roledescription','slide');
      s.setAttribute('aria-label',(n+1)+' of '+slides.length);
      var d=document.createElement('button'); d.type='button'; d.className='bc-quotes__dot';
      d.setAttribute('role','tab'); d.setAttribute('aria-label','Quote from '+s.querySelector('.bc-quotes__name').textContent);
      d.addEventListener('click',function(){go(n);restart();});
      dotsWrap.appendChild(d); dots.push(d);
    });

    var viewport=root.querySelector('.bc-quotes__viewport');
    function fit(){ var h=0; slides.forEach(function(s){ if(s.offsetHeight>h) h=s.offsetHeight; }); viewport.style.height=h+'px'; }
    window.addEventListener('resize',fit);
    if(document.fonts&&document.fonts.ready) document.fonts.ready.then(fit);
    window.addEventListener('load',fit);

    function go(n){
      i=(n+slides.length)%slides.length;
      slides.forEach(function(s,k){s.classList.toggle('is-active',k===i); s.setAttribute('aria-hidden',k===i?'false':'true');});
      dots.forEach(function(d,k){d.setAttribute('aria-selected',k===i?'true':'false');});
      fit();
    }
    function restart(){ stop(); if(!reduce) timer=setInterval(function(){go(i+1)},5000); }
    function stop(){ if(timer){clearInterval(timer);timer=null;} }

    root.querySelectorAll('.bc-quotes__btn').forEach(function(b){
      b.addEventListener('click',function(){go(i+Number(b.dataset.dir));restart();});
    });
    root.addEventListener('mouseenter',stop); root.addEventListener('mouseleave',restart);
    root.addEventListener('focusin',stop); root.addEventListener('focusout',restart);
    root.addEventListener('keydown',function(e){
      if(e.key==='ArrowRight'){go(i+1);restart();} else if(e.key==='ArrowLeft'){go(i-1);restart();}
    });
    var x0=null;
    root.addEventListener('touchstart',function(e){x0=e.touches[0].clientX;},{passive:true});
    root.addEventListener('touchend',function(e){
      if(x0===null) return; var dx=e.changedTouches[0].clientX-x0; x0=null;
      if(Math.abs(dx)>45){go(i+(dx<0?1:-1));restart();}
    });
    go(0); restart();
  }
  [].forEach.call(document.querySelectorAll('.bc-quotes'),init);
})();
