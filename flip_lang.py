import re

with open("c:/Users/Alejandro1/Documents/roblox-portfolio/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Base changes
html = html.replace('lang="es"', 'lang="en"')
html = html.replace('langToggle">🌐 <span>EN</span>', 'langToggle">🌐 <span>ES</span>')

# 2. Swap flag
html = html.replace('<div class="logo-icon" data-en="🇺🇸">🇪🇸</div>', '<div class="logo-icon" data-es="🇪🇸">🇺🇸</div>')

# 3. Swap translations
swaps = [
    (r'<a href="#inicio" data-en="Home">Inicio</a>', r'<a href="#inicio" data-es="Inicio">Home</a>'),
    (r'<a href="#sobre-mi" data-en="Why Hire Me">Por qué yo</a>', r'<a href="#sobre-mi" data-es="Por qué yo">Why Hire Me</a>'),
    (r'<a href="#habilidades" data-en="Capabilities">Capacidades</a>', r'<a href="#habilidades" data-es="Capacidades">Capabilities</a>'),
    (r'<a href="#portafolio" data-en="Portfolio">Portafolio</a>', r'<a href="#portafolio" data-es="Portafolio">Portfolio</a>'),
    (r'<a href="#terminos" data-en="Terms">Términos</a>', r'<a href="#terminos" data-es="Términos">Terms</a>'),
    (r'<a href="#contacto" data-en="Contact">Contacto</a>', r'<a href="#contacto" data-es="Contacto">Contact</a>'),
    
    (r'<div class="hero-badge" data-en="<span class=\'dot\'></span> Available for projects">\s*<span class="dot"></span>\s*Disponible para proyectos y comisiones\s*</div>', 
     r'<div class="hero-badge" data-es="<span class=\'dot\'></span> Disponible para proyectos y comisiones"><span class="dot"></span> Available for projects & commissions</div>'),
    
    (r'<h1 class="hero-title" data-en="Crafting worlds<br><span class=\'gradient-text\'>in Roblox</span>">\s*Programador de Luau<br>\s*<span class="gradient-text">en Roblox</span>\s*</h1>',
     r'<h1 class="hero-title" data-es="Programador de Luau<br><span class=\'gradient-text\'>en Roblox</span>">Luau Programmer<br><span class="gradient-text">on Roblox</span></h1>'),
    
    (r'<p class="hero-description" data-en="Specialized developer creating immersive and unique experiences on Roblox\. From detailed maps to complex scripting systems — I turn ideas into games\.">\s*Desarrollador especializado en crear sistemas modulares y escalables en Roblox\. \s*Desde sistemas y mecanicas basicas hasta sistemas complejos de scripting\.\s*</p>',
     r'<p class="hero-description" data-es="Desarrollador especializado en crear sistemas modulares y escalables. Desde mecánicas básicas hasta sistemas limpios y optimizados.">Specialized Scripter building modular, scalable, and optimized systems. I focus on clean code and performance-driven game mechanics.</p>'),
    
    (r'<a href="#portafolio" class="btn-primary" data-en="View Projects <svg',
     r'<a href="#portafolio" class="btn-primary" data-es="Ver Proyectos <svg'),
    (r'Ver Proyectos\s*<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17l9.2-9.2M17 17V7.8H7.8"/></svg>', 
     r'View Projects\n            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17l9.2-9.2M17 17V7.8H7.8"/></svg>'),
    
    (r'<div class="section-label" data-en="Why Hire Me">Por Qué Contratarme</div>', r'<div class="section-label" data-es="Por Qué Contratarme">Why Hire Me</div>'),
    (r'<h3 data-en="Proven experience and <span class=\'gradient-text\'>quality results</span>"></h3>', r'<h3 data-es="Experiencia comprobada y <span class=\'gradient-text\'>resultados de calidad</span>">Proven experience and <span class="gradient-text">quality results</span></h3>'),
    
    (r'<p style="margin: 0; color: var\(--text-secondary\); font-size: 0.98rem; line-height: 1.7;" data-en="I am a Luau programmer specializing in modular, clean and scalable systems\.">Soy un programador de Luau especializado en sistemas modulares, limpios y escalables\.</p>',
     r'<p style="margin: 0; color: var(--text-secondary); font-size: 0.98rem; line-height: 1.7;" data-es="Soy un programador de Luau especializado en sistemas modulares, limpios y escalables.">I am a Luau programmer specializing in modular, clean, and highly scalable systems.</p>'),
    
    (r'<p style="margin: 0; color: var\(--text-secondary\); font-size: 0.98rem; line-height: 1.7;" data-en="I have a strong track record of writing easily expandable code that is simple for other developers to read and maintain\.">Tengo un historial sólido escribiendo código fácilmente expandible y simple de leer para otros desarrolladores\.</p>',
     r'<p style="margin: 0; color: var(--text-secondary); font-size: 0.98rem; line-height: 1.7;" data-es="Tengo un historial sólido escribiendo código fácilmente expandible y simple de leer para otros desarrolladores.">I have a proven track record of writing easily expandable, DRY code that other developers can seamlessly read and maintain.</p>'),
    
    (r'<p style="margin: 0; color: var\(--text-secondary\); font-size: 0.98rem; line-height: 1.7;" data-en="I prioritize smooth communication, keeping clients up-to-date with consistent progress reports\.">Priorizo una comunicación fluida, manteniendo a los clientes informados con reportes de progreso constantes\.</p>',
     r'<p style="margin: 0; color: var(--text-secondary); font-size: 0.98rem; line-height: 1.7;" data-es="Priorizo una comunicación fluida, manteniendo a los clientes informados con reportes de progreso constantes.">I prioritize fluid communication, providing clients with consistent status updates and transparent progress tracking.</p>'),
    
    (r'<div class="section-label" data-en="Pricing">Precios</div>', r'<div class="section-label" data-es="Precios">Pricing</div>'),
    (r'<h2 class="section-title" data-en="My <span class=\'highlight\'>Services</span>">Mis <span class="highlight">Servicios</span></h2>', r'<h2 class="section-title" data-es="Mis <span class=\'highlight\'>Servicios</span>">My <span class="highlight">Services</span></h2>'),
    
    (r'<h3 data-en="Roblox Scripting" style="margin: 0; font-size: 1.05rem; font-weight: 600;">Roblox Scripting</h3>', r'<h3 data-es="Roblox Scripting" style="margin: 0; font-size: 1.05rem; font-weight: 600;">Roblox Scripting</h3>'),
    (r'data-en="from \$6/500Rbx depending on complexity">desde \$6/500Rbx dependiendo la complejidad</span>', r'data-es="desde $6/500Rbx dependiendo la complejidad">from $6/500Rbx depending on complexity</span>'),
    
    (r'<h3 data-en="Mechanics & Complex Systems" style="margin: 0; font-size: 1.05rem; font-weight: 600;">Mecanicas y Sistemas complejos</h3>', r'<h3 data-es="Mecánicas y Sistemas Complejos" style="margin: 0; font-size: 1.05rem; font-weight: 600;">Mechanics & Complex Systems</h3>'),
    (r'data-en="from \$3/200Rbx depending on complexity">desde \$3/200Rbx dependiendo la complejidad</span>', r'data-es="desde $3/200Rbx dependiendo la complejidad">from $3/200Rbx depending on complexity</span>'),
    
    (r'<div class="section-label" data-en="Capabilities">Capacidades</div>', r'<div class="section-label" data-es="Capacidades">Capabilities</div>'),
    (r'<h2 class="section-title" data-en="Scripting <span class=\'highlight\'>Skills</span>">Habilidades de <span class="highlight">Scripting</span></h2>', r'<h2 class="section-title" data-es="Habilidades de <span class=\'highlight\'>Scripting</span>">Scripting <span class="highlight">Skills</span></h2>'),
    
    (r'<h3 data-en="What I CAN script">Lo que SÍ programo</h3>', r'<h3 data-es="Lo que SÍ programo">What I CAN script</h3>'),
    (r'<li data-en="• Combat & Abilities">• Combate y Habilidades</li>', r'<li data-es="• Combate y Habilidades">• Combat & Abilities</li>'),
    (r'<li data-en="• Backend / DataStores">• Backend / DataStores</li>', r'<li data-es="• Backend / DataStores">• Backend / DataStores</li>'),
    (r'<li data-en="• UI Logic \(Frontend\)">• Lógica UI \(Frontend\)</li>', r'<li data-es="• Lógica UI (Frontend)">• UI Logic (Frontend)</li>'),
    (r'<li data-en="• Bug Fixing \(Debugging\)">• Corrección de Bugs</li>', r'<li data-es="• Corrección de Bugs">• Bug Fixing & Debugging</li>'),
    
    (r'<h3 data-en="What I DON\'T script">Lo que NO programo</h3>', r'<h3 data-es="Lo que NO programo">What I DON\'T script</h3>'),
    (r'<li data-en="• Complex A\.I\.">• I\.A\. compleja</li>', r'<li data-es="• I.A. compleja">• Complex A.I.</li>'),
    (r'<li data-en="• Vehicular Systems">• Sistemas vehiculares</li>', r'<li data-es="• Sistemas vehiculares">• Vehicular Systems</li>'),
    (r'<li data-en="• Advanced Weapon Systems">• Sistemas avanzados de armas</li>', r'<li data-es="• Sistemas avanzados de armas">• Advanced Weaponry</li>'),
    
    (r'<h3 data-en="Tools & Languages">Herramientas y Lenguajes</h3>', r'<h3 data-es="Herramientas y Lenguajes">Tools & Languages</h3>'),
    (r'<li data-en="• Luau \(Native Roblox\)">• Luau \(Nativo de Roblox\)</li>', r'<li data-es="• Luau (Nativo de Roblox)">• Luau (Native Roblox)</li>'),
    (r'<li data-en="• Knit Framework/Trove/Signal/Timer">• Knit Framework/Trove/Signal/Timer</li>', r'<li data-es="• Knit Framework/Trove/Signal">• Knit Framework/Trove/Signal</li>'),
    (r'<li data-en="• ProfileStore">• ProfileStore</li>', r'<li data-es="• ProfileStore / Datastores2">• ProfileStore / ReplicaService</li>'),
    
    (r'<div class="section-label" data-en="Portfolio">Portafolio</div>', r'<div class="section-label" data-es="Portafolio">Portfolio</div>'),
    (r'<h2 class="section-title" data-en="My Past <span class=\'highlight\'>Works</span>">Mis <span class="highlight">Trabajos anteriores</span></h2>', r'<h2 class="section-title" data-es="Mis <span class=\'highlight\'>Trabajos anteriores</span>">My Past <span class="highlight">Works</span></h2>'),
    
    (r'data-en="🔍 View Details">\s*🔍 Ver Detalles\s*</span>', r'data-es="🔍 Ver Detalles">🔍 View Details</span>'),
    
    (r'<h3 data-en="Simulator with Deployment System">Simulador con sistema de despliegue</h3>\s*<p data-en="Base simulator system with deployment mechanics and saving\.">Sistema de simulador base con mecánicas de despliegue y guardado\.</p>',
     r'<h3 data-es="Simulador con sistema de despliegue">Simulator Unboxing System</h3>\n            <p data-es="Sistema de simulador base con mecánicas de despliegue y guardado.">Built-from-scratch simulator foundation featuring deep unboxing mechanics and secure data-saving.</p>'),
     
    (r'data-title="Simulador con sistema de despliegue" data-desc="Sistema de simulador base con mecánicas de despliegue y guardado\." data-en-title="Simulator with Deployment System" data-en-desc="Base simulator system with deployment mechanics and saving\."',
     r'data-title="Simulator Unboxing System" data-desc="Built-from-scratch simulator foundation featuring deep unboxing mechanics and secure data-saving." data-es-title="Simulador con sistema de despliegue" data-es-desc="Sistema de simulador base con mecánicas de despliegue y guardado."'),
     
    (r'<h3 data-en="Inventory with Data Saving \(ProfileStore\)">Inventario con guardado de datos \(ProfileStore\)</h3>\s*<p data-en="Modular and secure inventory system to store items\.">Sistema de inventario modular y seguro para almacenar objetos\.</p>',
     r'<h3 data-es="Inventario seguro (ProfileStore)">Inventory System (ProfileStore)</h3>\n            <p data-es="Sistema de inventario modular y seguro.">Highly modular inventory architecture storing player data robustly via ProfileStore.</p>'),
     
    (r'data-title="Inventario con guardado de datos \(ProfileStore\)" data-desc="Sistema de inventario modular y seguro para almacenar objetos\." data-en-title="Inventory with Data Saving \(ProfileStore\)" data-en-desc="Modular and secure inventory system to store items\."',
     r'data-title="Inventory System (ProfileStore)" data-desc="Highly modular inventory architecture storing player data robustly via ProfileStore." data-es-title="Inventario seguro (ProfileStore)" data-es-desc="Sistema de inventario modular y seguro."'),
     
    (r'<h3 data-en="Shop with MarketplaceService">Tienda con MarketplaceService</h3>\s*<p data-en="Interactive shop interface integrated with in-game purchases\.">Interfaz de tienda interactiva integrada con compras del juego\.</p>',
     r'<h3 data-es="Tienda con MarketplaceService">MarketplaceService Shop</h3>\n            <p data-es="Interfaz de tienda interactiva integrada con compras.">Custom-programmed UI integrating developer products and gamepasses securely through Roblox\'s MarketplaceService.</p>'),
     
    (r'data-title="Tienda con MarketplaceService" data-desc="Interfaz de tienda interactiva integrada con compras del juego\." data-en-title="Shop with MarketplaceService" data-en-desc="Interactive shop interface integrated with in-game purchases\."',
     r'data-title="MarketplaceService Shop" data-desc="Custom-programmed UI integrating developer products and gamepasses securely through Roblox\'s MarketplaceService." data-es-title="Tienda con MarketplaceService" data-es-desc="Interfaz de tienda interactiva integrada con compras del juego."'),
     
    (r'<h3 data-en="Round System">Sistema de Rondas</h3>\s*<p data-en="Automated minigame loop with timer and teleportation\.">Ciclo de minijuegos automatizado con temporizador y teletransporte\.</p>',
     r'<h3 data-es="Sistema de Rondas">Automated Round System</h3>\n            <p data-es="Ciclo de minijuegos automatizado con temporizador y teletransporte.">Fully automated server-side minigame loop handling map loading, matchmaking, timers, and flawless teleportation.</p>'),
     
    (r'data-title="Sistema de Rondas" data-desc="Ciclo de minijuegos automatizado con temporizador y teletransporte\." data-en-title="Round System" data-en-desc="Automated minigame loop with timer and teleportation\."',
     r'data-title="Automated Round System" data-desc="Fully automated server-side minigame loop handling map loading, matchmaking, timers, and flawless teleportation." data-es-title="Sistema de Rondas" data-es-desc="Ciclo de minijuegos automatizado con temporizador y teletransporte."'),
     
    (r'<h3 data-en="Dynamic Gravity System">Sistema de Gravedad Dinámica</h3>\s*<p data-en="Gravity manipulation and advanced physics mechanics per round\.">Manipulación de gravedad y mecánicas físicas avanzadas por ronda\.</p>',
     r'<h3 data-es="Sistema de Gravedad Dinámica">Dynamic Gravity Mechanics</h3>\n            <p data-es="Manipulación de gravedad y mecánicas físicas por ronda.">Advanced physics manipulation script modifying gravity states seamlessly based on minigame requirements.</p>'),
     
    (r'data-title="Sistema de Gravedad Dinámica" data-desc="Manipulación de gravedad y mecánicas físicas avanzadas por ronda\." data-en-title="Dynamic Gravity System" data-en-desc="Gravity manipulation and advanced physics mechanics per round\."',
     r'data-title="Dynamic Gravity Mechanics" data-desc="Advanced physics manipulation script modifying gravity states seamlessly based on minigame requirements." data-es-title="Sistema de Gravedad Dinámica" data-es-desc="Manipulación de gravedad y mecánicas físicas por ronda."'),
     
    (r'<h3 data-en="Physical Ragdoll System">Sistema de Ragdoll Físico</h3>\s*<p data-en="Realistic and responsive ragdoll system for Roblox characters\.">Sistema de ragdoll realista y responsivo para personajes de Roblox\.</p>',
     r'<h3 data-es="Sistema de Ragdoll Físico">Physical Ragdoll System</h3>\n            <p data-es="Sistema de ragdoll realista y responsivo para personajes de Roblox.">Optimized character rig modification allowing high-performance, collision-accurate ragdolling upon events.</p>'),
     
    (r'data-title="Sistema de Ragdoll Físico" data-desc="Sistema de ragdoll realista y responsivo para personajes de Roblox\." data-en-title="Physical Ragdoll System" data-en-desc="Realistic and responsive ragdoll system for Roblox characters\."',
     r'data-title="Physical Ragdoll System" data-desc="Optimized character rig modification allowing high-performance, collision-accurate ragdolling upon events." data-es-title="Sistema de Ragdoll Físico" data-es-desc="Sistema de ragdoll realista y responsivo para personajes de Roblox."'),
     
    (r'<div class="section-label" data-en="Rules">Reglas</div>', r'<div class="section-label" data-es="Reglas">Rules</div>'),
    (r'<h2 class="section-title" data-en="Terms & <span class=\'highlight\'>Prices</span>">Términos y <span class="highlight">Precios</span></h2>', r'<h2 class="section-title" data-es="Términos y <span class=\'highlight\'>Precios</span>">Terms & <span class="highlight">Prices</span></h2>'),
    
    (r'<h3 data-en="Payment Methods">Métodos de Pago</h3>\s*<p data-en="I only accept USD through virtual Visas \(can be bought with PayPal/Credit Card\)\.">Solo acepto Paypal o Robux\.</p>',
     r'<h3 data-es="Métodos de Pago">Payment Methods</h3>\n          <p data-es="Solo acepto Paypal o Robux.">I exclusively accept PayPal (USD) or Robux via DevEx equivalent rates.</p>'),
     
    (r'<h3 data-en="Commission Policies">Políticas de Comisiones</h3>\s*<p data-en="I rarely accept long-term positions unless I strongly believe in the project\. Projects must be well-planned\.">Raramente acepto posiciones a largo plazo a menos que crea fuertemente en el proyecto\.</p>',
     r'<h3 data-es="Políticas de Comisiones">Commission Policies</h3>\n          <p data-es="Raramente acepto posiciones a largo plazo a menos que el proyecto tenga buena planificación.">I rarely take on long-term revshare positions unless the project exhibits excellent pre-planning and potential.</p>'),
     
    (r'<h3 data-en="Upfront Payment">Pago por Adelantado</h3>\s*<p data-en="A mandatory 50% upfront payment is required to protect against scams and wasted time\.">Se requiere un pago obligatorio del 50% por adelantado para proteger contra estafas y pérdida de tiempo\.</p>',
     r'<h3 data-es="Pago por Adelantado">Upfront Payment</h3>\n          <p data-es="Se requiere un pago del 50% por adelantado para asegurar el proyecto.">A mandatory 50% upfront payment is strictly required to secure my time and prevent potential delays from either side.</p>'),
     
    (r'<div class="section-label" data-en="Let\'s Talk">Hablemos</div>', r'<div class="section-label" data-es="Hablemos">Let\'s Talk</div>'),
    (r'<h2 class="section-title" data-en="Contact <span class=\'highlight\'>Me</span>">Contácta<span class="highlight">me</span></h2>', r'<h2 class="section-title" data-es="Contácta<span class=\'highlight\'>me</span>">Contact <span class="highlight">Me</span></h2>'),
    
    (r'<p class="reveal" data-en="Interested in working with me\? Send me a friend request or a direct message on Discord to discuss your project details and get a quote\." style="color: var\(--text-secondary\); margin-bottom: 30px; line-height: 1\.8;">¿Interesado en trabajar conmigo\? Envíame una solicitud de amistad o un mensaje directo en Discord para discutir los detalles de tu proyecto y obtener una cotización\.</p>',
     r'<p class="reveal" data-es="¿Interesado en trabajar conmigo? Envíame un DM en Discord para discutir cotizaciones." style="color: var(--text-secondary); margin-bottom: 30px; line-height: 1.8;">Ready to commission a system? Send me a direct message over on Discord so we can discuss deadlines and pricing.</p>'),
     
    (r'<span data-en="Discord Username" style="font-size: 0\.8rem; color: var\(--text-muted\);">Usuario de Discord</span>', r'<span data-es="Usuario de Discord" style="font-size: 0.8rem; color: var(--text-muted);">Discord Username</span>')
]

for src, tgt in swaps:
    html = re.sub(src, tgt, html)

# 4. Make script.js expect English by default
with open("c:/Users/Alejandro1/Documents/roblox-portfolio/script.js", "r", encoding="utf-8") as fs:
    js = fs.read()

js = js.replace("let currentLang = 'es';", "let currentLang = 'en';")
js_switcher_old = """  // ===== LANGUAGE SWITCHER =====
  const langToggle = document.getElementById('langToggle');
  let currentLang = 'es';

  if (langToggle) {
    langToggle.addEventListener('click', (e) => {
      e.preventDefault();
      currentLang = currentLang === 'es' ? 'en' : 'es';
      langToggle.querySelector('span').textContent = currentLang === 'es' ? 'EN' : 'ES';
      document.documentElement.lang = currentLang;

      document.querySelectorAll('[data-en]').forEach(el => {
        if (!el.hasAttribute('data-es')) {
          el.setAttribute('data-es', el.innerHTML);
        }
        el.innerHTML = el.getAttribute(`data-${currentLang}`);
      });
      
      document.querySelectorAll('.portfolio-item').forEach(item => {
        if (!item.hasAttribute('data-es-title')) {
           item.setAttribute('data-es-title', item.dataset.title);
           item.setAttribute('data-es-desc', item.dataset.desc);
        }
        item.dataset.title = item.getAttribute(`data-${currentLang}-title`) || item.dataset.title;
        item.dataset.desc = item.getAttribute(`data-${currentLang}-desc`) || item.dataset.desc;
      });
    });
  }"""
js_switcher_new = """  // ===== LANGUAGE SWITCHER =====
  const langToggle = document.getElementById('langToggle');
  let currentLang = 'en'; // default HTML is EN now

  if (langToggle) {
    langToggle.addEventListener('click', (e) => {
      e.preventDefault();
      currentLang = currentLang === 'en' ? 'es' : 'en';
      langToggle.querySelector('span').textContent = currentLang === 'en' ? 'ES' : 'EN';
      document.documentElement.lang = currentLang;

      document.querySelectorAll('[data-es]').forEach(el => {
        if (!el.hasAttribute('data-en')) {
          el.setAttribute('data-en', el.innerHTML);
        }
        el.innerHTML = el.getAttribute(`data-${currentLang}`);
      });
      
      document.querySelectorAll('.portfolio-item').forEach(item => {
        if (!item.hasAttribute('data-en-title')) {
           item.setAttribute('data-en-title', item.dataset.title);
           item.setAttribute('data-en-desc', item.dataset.desc);
        }
        item.dataset.title = item.getAttribute(`data-${currentLang}-title`) || item.dataset.title;
        item.dataset.desc = item.getAttribute(`data-${currentLang}-desc`) || item.dataset.desc;
      });
    });
  }
  
  // Disable memory-heavy autoplay videos unless visible
  const videos = document.querySelectorAll('video');
  const videoObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
          if (entry.isIntersecting) {
              entry.target.play().catch(e => console.log('Autoplay prevented:', e));
          } else {
              entry.target.pause();
          }
      });
  }, { threshold: 0.1 });
  
  videos.forEach(video => {
      video.removeAttribute('autoplay');
      videoObserver.observe(video);
  });
"""
  
js = js.replace(js_switcher_old, js_switcher_new)

with open("c:/Users/Alejandro1/Documents/roblox-portfolio/index.html", "w", encoding="utf-8") as f:
    f.write(html)
    
with open("c:/Users/Alejandro1/Documents/roblox-portfolio/script.js", "w", encoding="utf-8") as f:
    f.write(js)
