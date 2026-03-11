// Sticky header shadow
const header = document.querySelector('.header');
const onScroll = () => header.classList.toggle('is-scrolled', scrollY > 8);
addEventListener('scroll', onScroll, { passive: true });

// Mobile menu
const burger = document.getElementById('burger');
const nav    = document.getElementById('nav');
burger?.addEventListener('click', () => {
  const open = nav.classList.toggle('is-open');
  burger.setAttribute('aria-expanded', open);
});
nav?.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
  nav.classList.remove('is-open');
  burger?.setAttribute('aria-expanded', false);
}));

// Smooth scroll offset
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const target = document.querySelector(a.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    const offset = header?.offsetHeight ?? 0;
    scrollTo({ top: target.offsetTop - offset - 12, behavior: 'smooth' });
  });
});

// Scroll reveal
const css = document.createElement('style');
css.textContent = '.reveal{opacity:0;translate:0 20px;transition:opacity .45s ease,translate .45s ease}.reveal.in{opacity:1;translate:0 0}';
document.head.append(css);

new IntersectionObserver((entries, obs) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); obs.unobserve(e.target); }});
}, { threshold: .1 }).observe ||
new IntersectionObserver((entries, obs) => {
  entries.forEach((e, i) => {
    if (e.isIntersecting) {
      e.target.style.transitionDelay = `${(i % 3) * 70}ms`;
      e.target.classList.add('in');
      obs.unobserve(e.target);
    }
  });
}, { threshold: .1, rootMargin: '0px 0px -40px 0px' });

const revealObs = new IntersectionObserver((entries, obs) => {
  entries.forEach((e, i) => {
    if (e.isIntersecting) {
      e.target.style.transitionDelay = `${(i % 3) * 70}ms`;
      e.target.classList.add('in');
      obs.unobserve(e.target);
    }
  });
}, { threshold: .08, rootMargin: '0px 0px -30px 0px' });

document.querySelectorAll('.service-card, .review, .badge, .cred-item, .work-item')
  .forEach(el => { el.classList.add('reveal'); revealObs.observe(el); });
