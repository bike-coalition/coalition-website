/*
  Action Network text fixes for the Bike Share page petition. Moved unchanged from the petition Code block on the old /bike-share page.
  Petition: "Sign the petition" eyebrow, signature count and "Only N to go" line, "Add your name" heading, "ZIP Code" placeholder,
  "Add my name" button, "Bike Coalition" (not "Bicycle") in the sharing opt-in, and the thank-you headline and line.
  The letter-campaign parts (step labels, "Write my letter") only act on letter embeds; kept so the shared styling behaves as before.
*/
(function(){
  var HEAD = "Your name is on the petition.", LINE = "Thank you for standing up for bike share in San Diego County. Check your inbox for a confirmation.";
  function petTy(){
    document.querySelectorAll('.sdbc-action .can_embed.petition #can_embed_form.can_thank_you_wrap #can_thank_you').forEach(function(t){
      var h = t.querySelector('h1'); if(h && h.textContent !== HEAD) h.textContent = HEAD;
      var p = t.querySelector('.sdbc-ty'); if(p && p.textContent !== LINE) p.textContent = LINE;
    });
  }
  new MutationObserver(petTy).observe(document.documentElement,{childList:true,subtree:true});
  document.addEventListener('DOMContentLoaded', petTy); petTy();
})();
(function(){
  function fmt(n){ return Number(n).toLocaleString('en-US'); }
  function pet(){
    document.querySelectorAll('.sdbc-action .petition_full #can_embed_form').forEach(function(f){
      var box = f.querySelector(':scope > .clearfix') || f;
      if(!f.querySelector('.sdbc-eyebrow')){ var e = document.createElement('span'); e.className = 'sdbc-eyebrow'; e.textContent = 'Sign the petition'; box.insertBefore(e, box.firstChild); }
      var tot = f.querySelector('.action_status_running_total');
      if(tot && !tot.getAttribute('data-sdbc')){
        var m = tot.textContent.replace(/,/g,'').match(/(\d+)/);
        if(m){ var n = +m[1]; tot.innerHTML = '<strong>' + fmt(n) + '</strong>' + (n === 1 ? 'signature' : 'signatures'); tot.setAttribute('data-sdbc','1'); }
      }
      var goal = f.querySelector('.action_status_goal');
      if(goal && !goal.getAttribute('data-sdbc')){
        var gm = goal.textContent.replace(/,/g,'').match(/goal of (\d+)/i);
        var cm = (tot ? tot.textContent : '').replace(/,/g,'').match(/(\d+)/);
        if(gm && cm){ var G = +gm[1], left = G - (+cm[1]); goal.textContent = left > 0 ? 'Help us reach ' + fmt(G) + '. Only ' + fmt(left) + ' to go.' : 'We hit our goal of ' + fmt(G) + '. Keep the names coming.'; goal.setAttribute('data-sdbc','1'); }
      }
      var h4 = f.querySelector('.action_sidebar > h4'); if(h4 && h4.textContent !== 'Add your name') h4.textContent = 'Add your name';
      f.querySelectorAll('#d_sharing li em, #d_sharing li i, #d_sharing li strong').forEach(function(x){ if(/Bicycle Coalition/.test(x.textContent)) x.textContent = x.textContent.replace('San Diego County Bicycle Coalition','San Diego County Bike Coalition'); });
      f.querySelectorAll('input[placeholder="Zip/Postal Code *"]').forEach(function(i){ i.placeholder='ZIP Code *'; });
      var b = f.querySelector('.action_sidebar input[type=submit]'); if(b && b.value === 'Add Your Name') b.value = 'Add my name →';
    });
  }
  new MutationObserver(pet).observe(document.documentElement,{childList:true,subtree:true});
  document.addEventListener('DOMContentLoaded', pet); pet();
})();
(function(){
  var HEAD = "Your letter is on its way.", LINE = "Thank you for speaking up for safer streets. Check your inbox for a confirmation.";
  function ty(){
    document.querySelectorAll('.sdbc-action #can_embed_form.can_thank_you_wrap #can_thank_you').forEach(function(t){
      var h = t.querySelector('h1'); if(!h || h.getAttribute('data-sdbc')) return;
      h.textContent = HEAD; h.setAttribute('data-sdbc','1');
      var p = document.createElement('p'); p.className = 'sdbc-ty'; p.textContent = LINE; h.insertAdjacentElement('afterend', p);
    });
  }
  new MutationObserver(ty).observe(document.documentElement,{childList:true,subtree:true});
  document.addEventListener('DOMContentLoaded', ty); ty();
})();
(function(){
  var SUB2 = "<strong>Step 2 of 2:</strong> review your letter, make it your own if you like, then send it.";
  function step2(){
    document.querySelectorAll('.sdbc-action #can_embed_form').forEach(function(f){
      var on = !!f.querySelector('#subject, textarea#message');
      if(f.classList.contains('sdbc-step2') !== on) f.classList.toggle('sdbc-step2', on);
      var p = f.querySelector('.sdbc-sub'); if(on && p && p.getAttribute('data-step')!=='2'){ p.innerHTML = SUB2; p.setAttribute('data-step','2'); }
    });
  }
  new MutationObserver(step2).observe(document.documentElement,{childList:true,subtree:true});
  document.addEventListener('DOMContentLoaded', step2); step2();
})();
(function(){
  var COPY = {
    eyebrow: "Write your officials",
    sub: "<strong>Step 1 of 2:</strong> tell us who you are so your letter reaches the right people. Next, you'll review and send it.",
    subKnown: "<strong>Step 1 of 2:</strong> we have your address on file. Next, you'll review and send your letter.",
    button: "Write my letter →",
    optin: "Keep me posted on San Diego County Bike Coalition news and actions",
    sponsor: "San Diego County Bike Coalition"
  };
  function polish(root){
    var f = root.querySelector('#can_embed_form'); if(!f) return;
    var h4 = f.querySelector('h4.lined_after_title'); if(h4 && h4.textContent.trim()!==COPY.eyebrow){ h4.textContent = COPY.eyebrow; var inner=f.querySelector('#can_embed_form_inner'); inner.insertBefore(h4, inner.firstChild); }
    var h2 = f.querySelector('h2'); if(h2 && f.querySelector('#form_col1') && !f.querySelector('.sdbc-sub')){ var p=document.createElement('p'); p.className='sdbc-sub'; p.innerHTML=f.querySelector('#action_welcome_message')?COPY.subKnown:COPY.sub; h2.insertAdjacentElement('afterend', p); }
    var b = f.querySelector('#form_col2 input[type=submit]'); if(b && b.value==='Start Writing') b.value = COPY.button;
    var lab = f.querySelector('#d_sharing label'); if(lab){ var n=[].slice.call(lab.childNodes).filter(function(x){return x.nodeType===3 && /Opt in/.test(x.textContent)})[0]; if(n) n.textContent=' '+COPY.optin; }
    var sp = f.querySelector('.action_info_user a'); if(sp && sp.textContent!==COPY.sponsor) sp.textContent = COPY.sponsor;
    f.querySelectorAll('input[placeholder="Zip/Postal Code *"]').forEach(function(i){ i.placeholder='ZIP Code *'; });
  }
  function boot(){
    document.querySelectorAll('.sdbc-action').forEach(function(root){
      polish(root);
      new MutationObserver(function(){ polish(root); }).observe(root,{childList:true,subtree:true});
    });
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', boot); else boot();
})();
