// MENU DATA
const menuItems = [
  { id: 1, name: "Carnitas Taco", desc: "Slow-cooked pork", price: 3.50, icon: "🌮" },
  { id: 2, name: "Al Pastor", desc: "Marinated pork", price: 3.50, icon: "🌮" },
  { id: 3, name: "Carne Asada", desc: "Grilled beef", price: 4.00, icon: "🌮" },
  { id: 4, name: "Fish Taco", desc: "Crispy battered fish", price: 4.50, icon: "🐟" },
  { id: 5, name: "Chicken Taco", desc: "Grilled chicken", price: 3.25, icon: "🍗" },
  { id: 6, name: "Veggie Taco", desc: "Roasted vegetables", price: 3.00, icon: "🥬" },
  { id: 7, name: "Chorizo Taco", desc: "Spicy Mexican sausage", price: 3.75, icon: "🌭" },
  { id: 8, name: "Birria Taco", desc: "Slow-cooked beef stew", price: 4.25, icon: "🍲" },
];

// CART STATE
let cart = [];

// DOM ELEMENTS
const menuGrid = document.getElementById('menu-grid');
const cartBtn = document.getElementById('cart-btn');
const cartCount = document.getElementById('cart-count');
const cartSidebar = document.getElementById('cart-sidebar');
const cartOverlay = document.getElementById('cart-overlay');
const cartClose = document.getElementById('cart-close');
const cartItems = document.getElementById('cart-items');
const cartTotal = document.getElementById('cart-total');
const checkoutBtn = document.getElementById('checkout-btn');
const hero = document.getElementById('hero');
const heroContent = document.getElementById('hero-content');
const spotlight = document.getElementById('spotlight');
const heroBtn = document.getElementById('hero-btn');
const scrollProgress = document.getElementById('scroll-progress');

// ============================================
// ACETERNITY ANIMATIONS
// ============================================

// 1. MOUSE SPOTLIGHT EFFECT
function initSpotlight() {
  if (!hero || !spotlight) return;
  
  hero.addEventListener('mousemove', (e) => {
    const rect = hero.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width) * 100;
    const y = ((e.clientY - rect.top) / rect.height) * 100;
    spotlight.style.setProperty('--mouse-x', `${x}%`);
    spotlight.style.setProperty('--mouse-y', `${y}%`);
  });
}

// 2. 3D TILT EFFECT
function initTiltEffect() {
  if (!hero || !heroContent) return;
  
  const maxTilt = 10; // Maximum rotation in degrees
  
  hero.addEventListener('mousemove', (e) => {
    const rect = hero.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    
    const mouseX = e.clientX - centerX;
    const mouseY = e.clientY - centerY;
    
    const rotateY = (mouseX / (rect.width / 2)) * maxTilt;
    const rotateX = -(mouseY / (rect.height / 2)) * maxTilt;
    
    heroContent.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    heroContent.style.setProperty('--rotateX', `${rotateX}deg`);
    heroContent.style.setProperty('--rotateY', `${rotateY}deg`);
  });
  
  hero.addEventListener('mouseleave', () => {
    heroContent.style.transform = 'rotateX(0deg) rotateY(0deg)';
    heroContent.style.setProperty('--rotateX', '0deg');
    heroContent.style.setProperty('--rotateY', '0deg');
  });
}

// 3. MAGNETIC BUTTON EFFECT
function initMagneticButton() {
  if (!heroBtn) return;
  
  const magneticStrength = 0.3;
  
  heroBtn.addEventListener('mousemove', (e) => {
    const rect = heroBtn.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    
    const deltaX = (e.clientX - centerX) * magneticStrength;
    const deltaY = (e.clientY - centerY) * magneticStrength;
    
    heroBtn.style.transform = `translate(${deltaX}px, ${deltaY}px) scale(1.05)`;
  });
  
  heroBtn.addEventListener('mouseleave', () => {
    heroBtn.style.transform = 'translate(0, 0) scale(1)';
  });
}

// 4. SCROLL PROGRESS BAR
function initScrollProgress() {
  if (!scrollProgress) return;
  
  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollPercent = (scrollTop / docHeight) * 100;
    scrollProgress.style.width = `${scrollPercent}%`;
  });
}

// 5. INITIALIZE FLOATING PARTICLES (randomize start positions)
function initParticles() {
  const particles = document.querySelectorAll('.particle');
  particles.forEach((particle, index) => {
    // Randomize initial vertical position for variety
    const randomDelay = Math.random() * 5;
    const randomDuration = 10 + Math.random() * 10;
    particle.style.animationDelay = `${randomDelay}s`;
    particle.style.animationDuration = `${randomDuration}s`;
  });
}

// ============================================
// CART FUNCTIONALITY
// ============================================

// RENDER MENU
function renderMenu() {
  menuGrid.innerHTML = menuItems.map(item => `
    <div class="menu-item">
      <div class="menu-icon">${item.icon}</div>
      <h3>${item.name}</h3>
      <p class="desc">${item.desc}</p>
      <div class="price">$${item.price.toFixed(2)}</div>
      <button class="add-to-cart-btn" data-id="${item.id}">
        Add to Cart
      </button>
    </div>
  `).join('');

  // Add event listeners
  document.querySelectorAll('.add-to-cart-btn').forEach(btn => {
    btn.addEventListener('click', (e) => addToCart(parseInt(e.target.dataset.id)));
  });
}

// ADD TO CART
function addToCart(itemId) {
  const item = menuItems.find(i => i.id === itemId);
  const cartItem = cart.find(c => c.id === itemId);

  if (cartItem) {
    cartItem.qty++;
  } else {
    cart.push({ ...item, qty: 1 });
  }

  updateCart();
  openCart();
}

// UPDATE CART DISPLAY
function updateCart() {
  // Update count
  const totalItems = cart.reduce((sum, item) => sum + item.qty, 0);
  cartCount.textContent = totalItems;

  // Update items
  if (cart.length === 0) {
    cartItems.innerHTML = '<p class="empty-cart">Your cart is empty</p>';
  } else {
    cartItems.innerHTML = cart.map(item => `
      <div class="cart-item">
        <span class="cart-item-name">${item.name}</span>
        <div class="cart-item-qty">
          <button class="qty-btn minus" data-id="${item.id}">−</button>
          <span class="qty-display">${item.qty}</span>
          <button class="qty-btn plus" data-id="${item.id}">+</button>
        </div>
        <span class="cart-item-price">$${(item.price * item.qty).toFixed(2)}</span>
        <button class="cart-item-remove" data-id="${item.id}">✕</button>
      </div>
    `).join('');

    // Add qty listeners
    document.querySelectorAll('.qty-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id = parseInt(e.target.dataset.id);
        const isPlus = e.target.classList.contains('plus');
        updateQty(id, isPlus ? 1 : -1);
      });
    });

    // Add remove listeners
    document.querySelectorAll('.cart-item-remove').forEach(btn => {
      btn.addEventListener('click', (e) => {
        removeFromCart(parseInt(e.target.dataset.id));
      });
    });
  }

  // Update total
  const total = cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
  cartTotal.textContent = total.toFixed(2);
}

// UPDATE QUANTITY
function updateQty(itemId, change) {
  const item = cart.find(i => i.id === itemId);
  if (item) {
    item.qty += change;
    if (item.qty <= 0) {
      removeFromCart(itemId);
    } else {
      updateCart();
    }
  }
}

// REMOVE FROM CART
function removeFromCart(itemId) {
  cart = cart.filter(item => item.id !== itemId);
  updateCart();
}

// OPEN/CLOSE CART
function openCart() {
  cartSidebar.classList.add('show');
  cartOverlay.classList.add('show');
}

function closeCart() {
  cartSidebar.classList.remove('show');
  cartOverlay.classList.remove('show');
}

// EVENT LISTENERS
cartBtn.addEventListener('click', openCart);
cartClose.addEventListener('click', closeCart);
cartOverlay.addEventListener('click', closeCart);

// CHECKOUT
checkoutBtn.addEventListener('click', () => {
  if (cart.length === 0) {
    alert('Your cart is empty!');
    return;
  }

  const total = cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
  const itemsList = cart.map(item => `${item.qty}x ${item.name}`).join(', ');

  // OPTION 1: Stripe Payment Link (simple)
  // Replace with your actual Stripe payment link
  const stripeLink = `https://buy.stripe.com/test_YOUR_LINK_HERE?prefilled_email=customer@example.com`;

  // OPTION 2: For now, show an alert with order details
  alert(`Order Total: $${total.toFixed(2)}\n\nItems: ${itemsList}\n\nIn a real site, this would redirect to Stripe checkout.\n\nCall (555) 123-4567 to confirm your order!`);
});

// ============================================
// INITIALIZE
// ============================================

document.addEventListener('DOMContentLoaded', () => {
  renderMenu();
  initSpotlight();
  initTiltEffect();
  initMagneticButton();
  initScrollProgress();
  initParticles();
});
