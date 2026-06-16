/* ===== alexc308 Portfolio — Main Script ===== */

/* =============================================
   TRANSLATIONS
   ============================================= */
const i18n = {
  en: {
    'title':                'alexc308 — Roblox Dev',
    'nav.home':             'Home',
    'nav.about':            'About',
    'nav.skills':           'Skills',
    'nav.projects':         'Projects',
    'nav.terms':            'Terms',
    'nav.contact':          'Contact',
    'hero.greeting':        "Hello, I'm",
    'hero.subtitle':        'Roblox Luau Developer · Modular Systems · Clean Code',
    'hero.btn_projects':    'View Projects',
    'hero.btn_contact':     'Contact Me',
    'stats.experience':     'Years of experience',
    'stats.projects':       'Projects delivered',
    'stats.quality':        'Clean code',
    'stats.response':       'Response time',
    'about.title':          'About Me',
    'about.p1':             'Luau programmer specializing in modular, clean, and scalable systems built from the ground up.',
    'about.p2':             'Proven track record of writing DRY code that other developers can read, extend, and maintain with ease.',
    'about.p3':             'I prioritize fluid communication — regular status updates and transparent progress tracking throughout every project.',
    'about.p4':             'Available for commissions: systems, mechanics, backend, UI logic, and bug fixing.',
    'skills.title':         'Scripting Skills',
    'skills.stack':         'Tech Stack',
    'skills.can_title':     "What I CAN script",
    'skills.can1':          'Combat & Abilities',
    'skills.can2':          'Backend / DataStores',
    'skills.can3':          'UI Logic (Frontend)',
    'skills.can4':          'Bug Fixing & Debugging',
    'skills.can5':          'Round & Game systems',
    'skills.cant_title':    "What I DON'T script",
    'skills.cant1':         'Complex A.I.',
    'skills.cant2':         'Vehicle Systems',
    'skills.cant3':         'Advanced Weapon Systems',
    'skills.pricing_title': 'Pricing',
    'skills.price1':        'Basic Systems',
    'skills.price2':        'Intermediate Systems',
    'skills.price3':        'Advanced Systems',
    'portfolio.title':      'My Work / Examples',
    'terms.title':          'Terms & Conditions',
    'terms.payment_title':  'Payment Methods',
    'terms.payment_desc':   'I exclusively accept PayPal (USD) or Robux via DevEx equivalent rates.',
    'terms.policy_title':   'Commission Policy',
    'terms.policy_desc':    'I rarely take on long-term revshare unless the project shows excellent planning and potential.',
    'terms.upfront_title':  'Upfront Payment',
    'terms.upfront_desc':   'A mandatory 50% upfront is required to secure my time and prevent delays from either side.',
    'contact.title':        'Contact & Social Media',
    'contact.desc':         'Feel free to reach out via any of these platforms:',
    'contact.roblox_action':'View profile',
    'footer.rights':        'All rights reserved.',
  },
  es: {
    'title':                'alexc308 — Dev de Roblox',
    'nav.home':             'Inicio',
    'nav.about':            'Sobre mí',
    'nav.skills':           'Habilidades',
    'nav.projects':         'Proyectos',
    'nav.terms':            'Términos',
    'nav.contact':          'Contacto',
    'hero.greeting':        'Hola, soy',
    'hero.subtitle':        'Desarrollador Luau en Roblox · Sistemas Modulares · Código Limpio',
    'hero.btn_projects':    'Ver Proyectos',
    'hero.btn_contact':     'Contáctame',
    'stats.experience':     'Años de experiencia',
    'stats.projects':       'Proyectos entregados',
    'stats.quality':        'Código limpio',
    'stats.response':       'Tiempo de respuesta',
    'about.title':          'Sobre mí',
    'about.p1':             'Programador Luau especializado en sistemas modulares, limpios y escalables construidos desde cero.',
    'about.p2':             'Historial comprobado de código DRY que otros desarrolladores pueden leer, extender y mantener con facilidad.',
    'about.p3':             'Priorizo la comunicación fluida — actualizaciones regulares y seguimiento transparente del progreso en cada proyecto.',
    'about.p4':             'Disponible para comisiones: sistemas, mecánicas, backend, lógica de UI y corrección de bugs.',
    'skills.title':         'Habilidades de Scripting',
    'skills.stack':         'Herramientas',
    'skills.can_title':     'Lo que SÍ programo',
    'skills.can1':          'Combate y Habilidades',
    'skills.can2':          'Backend / DataStores',
    'skills.can3':          'Lógica UI (Frontend)',
    'skills.can4':          'Corrección de Bugs',
    'skills.can5':          'Sistemas de Rondas',
    'skills.cant_title':    'Lo que NO programo',
    'skills.cant1':         'I.A. compleja',
    'skills.cant2':         'Sistemas vehiculares',
    'skills.cant3':         'Sistemas avanzados de armas',
    'skills.pricing_title': 'Precios',
    'skills.price1':        'Sistemas básicos',
    'skills.price2':        'Sistemas intermedios',
    'skills.price3':        'Sistemas avanzados',
    'portfolio.title':      'Mis Trabajos / Ejemplos',
    'terms.title':          'Términos y Condiciones',
    'terms.payment_title':  'Métodos de Pago',
    'terms.payment_desc':   'Solo acepto PayPal (USD) o Robux mediante tarifas equivalentes a DevEx.',
    'terms.policy_title':   'Política de Comisiones',
    'terms.policy_desc':    'Raramente acepto posiciones a largo plazo a menos que el proyecto tenga excelente planificación.',
    'terms.upfront_title':  'Pago Anticipado',
    'terms.upfront_desc':   'Se requiere un pago anticipado obligatorio del 50% para asegurar mi tiempo.',
    'contact.title':        'Contacto y Redes Sociales',
    'contact.desc':         'Puedes contactarme por cualquiera de estas plataformas:',
    'contact.roblox_action':'Ver perfil',
    'footer.rights':        'Todos los derechos reservados.',
  }
};

let currentLang = localStorage.getItem('lang') || 'en';

function applyLanguage(lang) {
  currentLang = lang;
  localStorage.setItem('lang', lang);
  const dict = i18n[lang] || i18n['en'];

  // Update title
  document.title = dict['title'];

  // Update all [data-i18n] elements
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (dict[key] !== undefined) {
      el.textContent = dict[key];
    }
  });

  // Update html lang
  document.documentElement.lang = lang;
}

document.addEventListener('DOMContentLoaded', () => {

  // ===== YEAR =====
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // ===== LANGUAGE TOGGLE =====
  const langSelect = document.getElementById('langSelect');
  if (langSelect) {
    langSelect.value = currentLang;
    langSelect.addEventListener('change', () => {
      applyLanguage(langSelect.value);
    });
  }
  applyLanguage(currentLang);

  // ===== NAVBAR SCROLL EFFECT =====
  const navbar = document.getElementById('navbar');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 60) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }, { passive: true });

  // ===== MOBILE MENU TOGGLE =====
  const navToggle = document.getElementById('navToggle');
  const navLinks  = document.getElementById('navLinks');

  navToggle.addEventListener('click', () => {
    navToggle.classList.toggle('active');
    navLinks.classList.toggle('open');
  });

  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navToggle.classList.remove('active');
      navLinks.classList.remove('open');
    });
  });

  // ===== SMOOTH SCROLL =====
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href === '#') return;
      e.preventDefault();
      const target = document.querySelector(href);
      if (target) {
        const offset = 80;
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  // ===== SCROLL PROGRESS BAR =====
  const progressBar = document.getElementById('scroll-progress');
  window.addEventListener('scroll', () => {
    const total   = document.documentElement.scrollHeight - window.innerHeight;
    const current = window.scrollY;
    progressBar.style.width = (total > 0 ? (current / total) * 100 : 0) + '%';
  }, { passive: true });

  // ===== BACK TO TOP =====
  const backBtn = document.getElementById('back-to-top');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
      backBtn.classList.add('visible');
    } else {
      backBtn.classList.remove('visible');
    }
  }, { passive: true });

  backBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  // ===== ACTIVE NAV LINK ON SCROLL =====
  const sections = document.querySelectorAll('section[id]');

  function updateActiveLink() {
    const scrollY = window.scrollY + 120;
    let current = '';
    sections.forEach(section => {
      if (scrollY >= section.offsetTop) {
        current = section.getAttribute('id');
      }
    });
    document.querySelectorAll('.nav-link').forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === '#' + current) {
        link.classList.add('active');
      }
    });
  }

  window.addEventListener('scroll', updateActiveLink, { passive: true });
  updateActiveLink();

  // ===== FADE-IN / REVEAL ANIMATIONS =====
  const fadeEls = document.querySelectorAll('.fade-in');

  const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        fadeObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.08,
    rootMargin: '0px 0px -40px 0px'
  });

  fadeEls.forEach(el => fadeObserver.observe(el));

  // ===== LIGHTBOX =====
  const lightbox     = document.getElementById('lightbox');
  const lightboxImg  = document.getElementById('lightboxImg');
  const lightboxVid  = document.getElementById('lightboxVid');
  const lightboxTitle = document.getElementById('lightboxTitle');
  const lightboxDesc  = document.getElementById('lightboxDesc');
  const lightboxClose = document.getElementById('lightboxClose');
  const lightboxPrev  = document.getElementById('lightboxPrev');
  const lightboxNext  = document.getElementById('lightboxNext');

  let currentIdx = 0;
  let items = [];

  function buildItems() {
    items = [];
    document.querySelectorAll('.portfolio-item').forEach(item => {
      items.push({
        img:   item.dataset.img,
        title: item.dataset.title,
        desc:  item.dataset.desc || ''
      });
    });
  }

  function openLightbox(idx) {
    buildItems();
    currentIdx = idx;
    renderLightbox();
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function renderLightbox() {
    const d = items[currentIdx];
    if (!d) return;
    if (d.img.endsWith('.mp4')) {
      lightboxImg.style.display = 'none';
      lightboxVid.style.display = 'block';
      lightboxVid.src = d.img;
      lightboxVid.play().catch(() => {});
    } else {
      lightboxVid.style.display = 'none';
      lightboxVid.pause();
      lightboxImg.style.display = 'block';
      lightboxImg.src  = d.img;
      lightboxImg.alt  = d.title;
    }
    lightboxTitle.textContent = d.title;
    lightboxDesc.textContent  = d.desc;
  }

  function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
    lightboxVid.pause();
  }

  document.querySelectorAll('.portfolio-item').forEach((item, idx) => {
    item.addEventListener('click', () => openLightbox(idx));
  });

  lightboxClose.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', e => { if (e.target === lightbox) closeLightbox(); });

  lightboxPrev.addEventListener('click', e => {
    e.stopPropagation();
    currentIdx = (currentIdx - 1 + items.length) % items.length;
    renderLightbox();
  });

  lightboxNext.addEventListener('click', e => {
    e.stopPropagation();
    currentIdx = (currentIdx + 1) % items.length;
    renderLightbox();
  });

  document.addEventListener('keydown', e => {
    if (!lightbox.classList.contains('active')) return;
    if (e.key === 'Escape')     closeLightbox();
    if (e.key === 'ArrowLeft')  { currentIdx = (currentIdx - 1 + items.length) % items.length; renderLightbox(); }
    if (e.key === 'ArrowRight') { currentIdx = (currentIdx + 1) % items.length; renderLightbox(); }
  });

});
