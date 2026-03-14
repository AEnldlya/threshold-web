/* =====================================
   HEADER SCROLL STATE
===================================== */
const header = document.querySelector('.site-header');
window.addEventListener('scroll', () => {
  header.classList.toggle('scrolled', window.scrollY > 20);
}, { passive: true });

/* =====================================
   MOBILE MENU
===================================== */
const menuToggle = document.getElementById('menu-toggle');
const navLinks   = document.getElementById('main-nav');

if (menuToggle && navLinks) {
  menuToggle.addEventListener('click', () => {
    const isOpen = menuToggle.getAttribute('aria-expanded') === 'true';
    menuToggle.setAttribute('aria-expanded', String(!isOpen));
    navLinks.classList.toggle('nav-open', !isOpen);
  });

  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('nav-open');
      menuToggle.setAttribute('aria-expanded', 'false');
    });
  });
}

/* =====================================
   SMOOTH SCROLL (offsets for sticky header)
===================================== */
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const id = a.getAttribute('href');
    if (id === '#') return;
    const target = document.querySelector(id);
    if (!target) return;
    e.preventDefault();
    const offset = header ? header.offsetHeight + 12 : 0;
    window.scrollTo({
      top: target.getBoundingClientRect().top + window.scrollY - offset,
      behavior: 'smooth'
    });
  });
});

/* =====================================
   INTERSECTION OBSERVER — FADE IN
===================================== */
const style = document.createElement('style');
style.textContent = `
  .anim { opacity: 0; transform: translateY(24px); transition: opacity .5s ease, transform .5s ease; }
  .anim.in { opacity: 1; transform: none; }
`;
document.head.appendChild(style);

const targets = document.querySelectorAll(
  '.service-item, .review-card, .process-step, .stat-card, .credential, .contact-method'
);

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

targets.forEach((el, i) => {
  el.classList.add('anim');
  el.style.transitionDelay = `${(i % 4) * 80}ms`;
  observer.observe(el);
});

/* =====================================
   FORM — SUBMIT FEEDBACK
===================================== */
const form = document.querySelector('.contact-form');
if (form) {
  form.addEventListener('submit', () => {
    const btn = form.querySelector('button[type="submit"]');
    if (btn) { btn.disabled = true; btn.textContent = 'Sending…'; }
  });
}
