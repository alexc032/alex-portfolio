/* ===== DevRBX Portfolio — Main Script ===== */

document.addEventListener('DOMContentLoaded', () => {

  // ===== NAVBAR SCROLL EFFECT =====
  const navbar = document.getElementById('navbar');
  let lastScroll = 0;

  window.addEventListener('scroll', () => {
    const currentScroll = window.scrollY;
    if (currentScroll > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
    lastScroll = currentScroll;
  });

  // ===== MOBILE MENU TOGGLE =====
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');

  navToggle.addEventListener('click', () => {
    navToggle.classList.toggle('active');
    navLinks.classList.toggle('open');
  });

  // Close mobile menu on link click
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navToggle.classList.remove('active');
      navLinks.classList.remove('open');
    });
  });

  // ===== SMOOTH SCROLL =====
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        const offset = 80;
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  // ===== SCROLL REVEAL ANIMATIONS =====
  const revealElements = document.querySelectorAll('.reveal');

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });

  revealElements.forEach(el => revealObserver.observe(el));



  // ===== PORTFOLIO ITEMS (for lightbox) =====
  const portfolioItems = document.querySelectorAll('.portfolio-item');

  // ===== LIGHTBOX =====
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxVid = document.getElementById('lightboxVid');
  const lightboxTitle = document.getElementById('lightboxTitle');
  const lightboxDesc = document.getElementById('lightboxDesc');
  const lightboxClose = document.getElementById('lightboxClose');
  const lightboxPrev = document.getElementById('lightboxPrev');
  const lightboxNext = document.getElementById('lightboxNext');

  let currentLightboxIndex = 0;
  let lightboxData = [];

  // Build lightbox data
  function buildLightboxData() {
    lightboxData = [];
    document.querySelectorAll('.portfolio-item').forEach(item => {
      if (item.style.display !== 'none') {
        lightboxData.push({
          img: item.dataset.img,
          title: item.dataset.title,
          desc: item.dataset.desc
        });
      }
    });
  }

  // Open lightbox
  portfolioItems.forEach(item => {
    item.addEventListener('click', () => {
      buildLightboxData();
      const clickedImg = item.dataset.img;
      currentLightboxIndex = lightboxData.findIndex(d => d.img === clickedImg);
      if (currentLightboxIndex === -1) currentLightboxIndex = 0;
      updateLightbox();
      lightbox.classList.add('active');
      document.body.style.overflow = 'hidden';
    });
  });

  function updateLightbox() {
    const data = lightboxData[currentLightboxIndex];
    if (!data) return;
    
    if (data.img.endsWith('.mp4')) {
      lightboxImg.style.display = 'none';
      lightboxVid.style.display = 'block';
      lightboxVid.src = data.img;
      lightboxVid.play();
    } else {
      lightboxVid.style.display = 'none';
      lightboxImg.style.display = 'block';
      lightboxVid.pause();
      lightboxImg.src = data.img;
      lightboxImg.alt = data.title;
    }
    
    lightboxTitle.textContent = data.title;
    lightboxDesc.textContent = data.desc;
  }

  // Close lightbox
  function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
    if (lightboxVid) lightboxVid.pause();
  }

  lightboxClose.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) closeLightbox();
  });

  // Navigation
  lightboxPrev.addEventListener('click', (e) => {
    e.stopPropagation();
    currentLightboxIndex = (currentLightboxIndex - 1 + lightboxData.length) % lightboxData.length;
    updateLightbox();
  });

  lightboxNext.addEventListener('click', (e) => {
    e.stopPropagation();
    currentLightboxIndex = (currentLightboxIndex + 1) % lightboxData.length;
    updateLightbox();
  });

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {
    if (!lightbox.classList.contains('active')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') {
      currentLightboxIndex = (currentLightboxIndex - 1 + lightboxData.length) % lightboxData.length;
      updateLightbox();
    }
    if (e.key === 'ArrowRight') {
      currentLightboxIndex = (currentLightboxIndex + 1) % lightboxData.length;
      updateLightbox();
    }
  });

  // ===== ACTIVE NAV LINK ON SCROLL =====
  const sections = document.querySelectorAll('section[id]');

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY + 100;

    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      const sectionId = section.getAttribute('id');

      if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
        navLinks.querySelectorAll('a').forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + sectionId) {
            link.style.color = 'var(--text-primary)';
          } else if (!link.classList.contains('nav-cta')) {
            link.style.color = '';
          }
        });
      }
    });
  });

  // Particles removed for minimal design

});
