// Professional scroll animations using Intersection Observer
// Triggers smooth fade-in, slide-in, and scale animations as elements enter viewport

const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            // Add active class to trigger animation
            entry.target.classList.add('active');
            // Don't unobserve - keep the animation
        }
    });
}, observerOptions);

// Observe all animated elements on page load
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll(
        '.fade-in, .slide-in-left, .slide-in-right, .scale-in, .flip-up'
    );
    
    animatedElements.forEach(el => {
        observer.observe(el);
    });
});

// Navigation link active state
const navLinks = document.querySelectorAll('.nav-link');

// Set active link based on current page
function setActiveNavLink() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPage || (currentPage === '' && href === 'index.html')) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

// Set active on load
setActiveNavLink();

// Update active state on navigation
navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        // Check if it's an internal link
        const href = link.getAttribute('href');
        if (!href.startsWith('http') && href !== '#') {
            navLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
        }
    });
});

// Smooth scroll behavior for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#' && document.querySelector(href)) {
            e.preventDefault();
            document.querySelector(href).scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
