#!/usr/bin/env python3
"""Generate zone landing pages for ChiclanaReformas"""

import os

ZONES = [
    {
        "slug": "reformas-novo-sancti-petri",
        "title_tag": "Reformas en Novo Sancti Petri | ChiclanaReformas",
        "meta_desc": "Reformas de viviendas en Novo Sancti Petri, Chiclana. Segundas residencias, chalets, piscinas y reformas integrales. Presupuesto gratuito ☎ 856 634 541",
        "canonical": "https://reformaschiclana.es/reformas-novo-sancti-petri.html",
        "zone": "Novo Sancti Petri",
        "zone_tag": "📍 Novo Sancti Petri",
        "h1_span": "Novo Sancti Petri",
        "lead": "Reformas de segundas residencias y chalets en Novo Sancti Petri. Atendemos a propietarios de toda España con coordinación a distancia.",
        "content": """<h2>Reformas en Novo Sancti Petri</h2>
<p>Novo Sancti Petri es la zona residencial por excelencia de Chiclana de la Frontera. Con sus urbanizaciones de chalets, apartamentos y residencias de lujo cerca del campo de golf y de la playa, es un área con constante demanda de reformas y mejoras.</p>
<p>En ChiclanaReformas somos especialistas en reformas para propietarios que no residen permanentemente en Novo Sancti Petri. Sabemos que muchos de nuestros clientes son de Madrid, País Vasco, Cataluña o del extranjero, y coordinamos todo el proceso de reforma para que no tengas que desplazarte.</p>

<h2>¿Qué reformas realizamos en Novo Sancti Petri?</h2>
<ul>
<li>Reformas integrales de chalets y viviendas</li>
<li>Reformas de cocinas y baños en segundas residencias</li>
<li>Construcción de piscinas privadas</li>
<li>Reforma de terrazas, porches y pérgolas</li>
<li>Pintura exterior y tratamiento de fachadas</li>
<li>Instalación de suelos, alicatados y carpintería</li>
<li>Acondicionamiento de jardines y zonas exteriores</li>
</ul>

<h2>Segundas residencias en Novo Sancti Petri</h2>
<p>Gran parte de nuestro trabajo en Novo Sancti Petri se centra en segundas residencias que necesitan actualizarse: cocinas antiguas, baños deteriorados por la humedad marina, terrazas sin cerramiento o piscinas que necesitan una renovación completa.</p>
<p>Utilizamos materiales especialmente seleccionados para resistir el ambiente costero: porcelánicos de alta resistencia, maderas tropicales tratadas, aceros inoxidables y pinturas con protección UV y antihongos.</p>""",
        "faq_q": [
            "¿Hacéis reformas para propietarios que no están en Novo Sancti Petri?",
            "¿Cuánto cuesta reformar un chalet en Novo Sancti Petri?",
            "¿Cuánto tarda una reforma en Novo Sancti Petri?",
            "¿Instaláis piscinas en Novo Sancti Petri?"
        ],
        "faq_a": [
            "Sí, la mayoría de nuestros clientes en Novo Sancti Petri no residen permanentemente allí. Coordinamos todo a distancia con actualizaciones fotográficas y videollamadas.",
            "Depende del tamaño y tipo de reforma. Un chalet mediano puede necesitar entre 15.000€ y 80.000€ para una reforma integral completa.",
            "Depende del alcance: una reforma parcial puede hacerse en 2-4 semanas. Una reforma integral de chalet puede requerir 2-3 meses.",
            "Sí, construimos piscinas a medida en Novo Sancti Petri. Gestionamos también los permisos necesarios del Ayuntamiento de Chiclana."
        ]
    },
    {
        "slug": "reformas-la-barrosa",
        "title_tag": "Reformas en La Barrosa | ChiclanaReformas",
        "meta_desc": "Reformas de viviendas en La Barrosa, Chiclana de la Frontera. Casas en primera línea de playa, apartamentos y segundas residencias. ☎ 856 634 541",
        "canonical": "https://reformaschiclana.es/reformas-la-barrosa.html",
        "zone": "La Barrosa",
        "zone_tag": "🏖️ La Barrosa",
        "h1_span": "La Barrosa",
        "lead": "Reformas en La Barrosa, la joya costera de Chiclana. Casas de playa, apartamentos y segundas residencias con acabados resistentes al mar.",
        "content": """<h2>Reformas en La Barrosa</h2>
<p>La Barrosa es una de las playas más emblemáticas de la costa de Cádiz, y sus urbanizaciones albergan miles de viviendas que, con el paso de los años, necesitan reformas y actualizaciones. Desde apartamentos en primera línea hasta chalets en urbanizaciones tranquilas, en ChiclanaReformas cubrimos todo tipo de propiedades.</p>
<p>El entorno marino de La Barrosa exige materiales y técnicas específicas. La salinidad, la humedad y la exposición solar constante son factores que consideramos en cada reforma para garantizar la máxima durabilidad.</p>

<h2>¿Qué reformas hacemos en La Barrosa?</h2>
<ul>
<li>Reformas integrales de viviendas junto a la playa</li>
<li>Renovación de cocinas y baños con materiales costeros</li>
<li>Cerramiento de terrazas con cristal tipo cortina</li>
<li>Pintura exterior con productos anti-salinidad</li>
<li>Tratamiento de humedades causadas por la proximidad al mar</li>
<li>Instalación de ventanas de climalit y carpintería de aluminio</li>
<li>Reforma de porches y zonas de estar al aire libre</li>
</ul>

<h2>Reformas para casas de verano en La Barrosa</h2>
<p>Muchos propietarios de La Barrosa utilizan su vivienda únicamente en verano. Esto implica que la casa permanece cerrada durante meses, lo que puede provocar deterioros por humedad. Recomendamos reformas con materiales de alta resistencia y sistemas de ventilación que protejan la vivienda cuando no está ocupada.</p>""",
        "faq_q": [
            "¿Cuánto cuesta reformar una casa en La Barrosa?",
            "¿Usáis materiales resistentes a la salinidad?",
            "¿Podéis reformar mi casa si no estoy en Chiclana?",
            "¿Instaláis cerramientos de terraza en La Barrosa?"
        ],
        "faq_a": [
            "Depende de la vivienda: un apartamento puede reformarse desde 5.000€ y un chalet desde 15.000€. Te hacemos un presupuesto personalizado.",
            "Sí, es prioritario en La Barrosa. Usamos porcelánicos, aluminio lacado, acero inoxidable y pinturas con protección especial contra la salinidad.",
            "Sí, coordinamos reformas a distancia con actualizaciones por fotos y WhatsApp. Es muy habitual en La Barrosa.",
            "Sí, cerramos terrazas con cortinas de cristal, paneles correderos y oscilobatientes. Maximizas el espacio habitable frente al mar."
        ]
    },
    {
        "slug": "reformas-pago-del-humo",
        "title_tag": "Reformas en Pago del Humo, Chiclana | ChiclanaReformas",
        "meta_desc": "Reformas de viviendas en Pago del Humo, Chiclana de la Frontera. Cortijos, chalets y casas rurales. Presupuesto gratuito ☎ 856 634 541",
        "canonical": "https://reformaschiclana.es/reformas-pago-del-humo.html",
        "zone": "Pago del Humo",
        "zone_tag": "🌿 Pago del Humo",
        "h1_span": "Pago del Humo",
        "lead": "Reformas en Pago del Humo. Cortijos, chalets y viviendas rurales con el carácter auténtico de la campiña chiclanera.",
        "content": """<h2>Reformas en Pago del Humo</h2>
<p>El Pago del Humo es una de las zonas más características de Chiclana de la Frontera. Con sus cortijos, casas rurales, chalets y parcelas, ofrece un entorno tranquilo y natural muy diferente al ambiente turístico de la costa. Es una zona ideal para quienes buscan paz y contacto con la naturaleza.</p>
<p>En ChiclanaReformas tenemos amplia experiencia reformando propiedades en el Pago del Humo. Desde la rehabilitación de cortijos tradicionales hasta la construcción de extensiones y mejoras en chalets modernos, adaptamos cada proyecto al carácter de la zona.</p>

<h2>¿Qué reformas hacemos en el Pago del Humo?</h2>
<ul>
<li>Rehabilitación y reforma de cortijos tradicionales</li>
<li>Reformas integrales de chalets y casas adosadas</li>
<li>Ampliaciones de vivienda y construcciones anexas</li>
<li>Construcción de piscinas en parcelas rústicas</li>
<li>Reforma de porches, terrazas y zonas exteriores</li>
<li>Acondicionamiento de techos y cubiertas</li>
<li>Cercado de parcelas y muros de contención</li>
</ul>

<h2>Rehabilitación de cortijos</h2>
<p>El Pago del Humo conserva varios cortijos que merecen ser rehabilitados. En ChiclanaReformas respetamos la arquitectura tradicional gaditana mientras incorporamos instalaciones modernas: fontanería, electricidad, aislamiento térmico y sistemas de climatización que hacen habitable estas propiedades con todo el encanto del pasado.</p>""",
        "faq_q": [
            "¿Reformáis cortijos antiguos en el Pago del Humo?",
            "¿Cuánto cuesta reformar una casa en el Pago del Humo?",
            "¿Construís piscinas en parcelas del Pago del Humo?",
            "¿Necesitáis algún permiso especial?"
        ],
        "faq_a": [
            "Sí, rehabilitamos cortijos respetando la arquitectura tradicional e instalando comodidades modernas. Es uno de nuestros proyectos más rewarding.",
            "Depende del tipo de propiedad: un cortijo puede requerir entre 20.000€ y 100.000€ según el estado. Un chalet estándar desde 10.000€.",
            "Sí, construimos piscinas a medida en parcelas del Pago del Humo. Evaluamos el terreno y te asesoramos sobre el mejor tipo de piscina.",
            "Para obras importantes en zona rústica pueden necesitarse permisos adicionales. Nosotros gestionamos toda la tramitación con el Ayuntamiento."
        ]
    },
    {
        "slug": "reformas-campano",
        "title_tag": "Reformas en Campano, Chiclana | ChiclanaReformas",
        "meta_desc": "Reformas de viviendas en Campano, Chiclana de la Frontera. Viviendas, locales y reformas integrales. Presupuesto gratuito ☎ 856 634 541",
        "canonical": "https://reformaschiclana.es/reformas-campano.html",
        "zone": "Campano",
        "zone_tag": "🏘️ Campano",
        "h1_span": "Campano",
        "lead": "Reformas en Campano, la zona en expansión de Chiclana. Viviendas nuevas, reformas integrales y acondicionamiento completo.",
        "content": """<h2>Reformas en Campano</h2>
<p>Campano es una de las zonas con mayor crecimiento residencial de Chiclana de la Frontera. Con nuevas urbanizaciones, viviendas unifamiliares y parcelas en desarrollo, es un área donde las reformas y mejoras de vivienda están en constante demanda.</p>
<p>En ChiclanaReformas ofrecemos todo tipo de servicios de reforma en Campano, desde reformas integrales para viviendas nuevas que necesitan personalización hasta actualizaciones y mejoras en propiedades ya existentes.</p>

<h2>¿Qué reformas hacemos en Campano?</h2>
<ul>
<li>Reformas integrales de viviendas nuevas y de segunda mano</li>
<li>Personalización de viviendas en urbanizaciones nuevas</li>
<li>Reformas de cocinas y baños</li>
<li>Construcción de piscinas en parcelas</li>
<li>Acondicionamiento de jardines y exteriores</li>
<li>Pintura interior y exterior</li>
<li>Instalación de suelos, revestimientos y carpintería</li>
</ul>

<h2>Urbanizaciones nuevas en Campano</h2>
<p>Campano cuenta con varias urbanizaciones nuevas donde los propietarios suelen querer personalizar su vivienda desde el momento de la entrega. Adaptamos cocinas, baños, suelos y acabados al gusto de cada cliente, trabajando con los materiales y colores que prefieras.</p>""",
        "faq_q": [
            "¿Cuánto cuesta reformar una casa en Campano?",
            "¿Personalizáis viviendas nuevas en Campano?",
            "¿Construís piscinas en Campano?",
            "¿Cuánto tardáis en responder al presupuesto?"
        ],
        "faq_a": [
            "Depende de la vivienda y el tipo de reforma. Una cocina desde 3.000€, un baño desde 2.500€ y una reforma integral desde 8.000€.",
            "Sí, trabajamos con propietarios de viviendas nuevas en Campano para personalizarlas según sus preferencias de diseño y materiales.",
            "Sí, construimos piscinas a medida en las parcelas de Campano. Evaluamos el terreno y te presentamos opciones adaptadas a tu presupuesto.",
            "Respondemos en menos de 24 horas tras la visita. Te contactamos para entregarte el presupuesto detallado sin compromiso."
        ]
    }
]

def footer():
    return '''<footer class="site-footer">
  <div class="site-footer-wrap">
    <div class="site-footer-cols">
      <div class="footer-about">
        <a href="/" class="brand">Chiclana<em>Reformas</em></a>
        <p>Empresa de reformas en Chiclana de la Frontera con más de 15 años de experiencia.</p>
        <div class="footer-contact-info">
          <strong>Dirección:</strong> Calle de las Flores, 12 — 11130 Chiclana de la Frontera, Cádiz<br>
          <strong>Teléfono:</strong> <a href="tel:856634541">856 634 541</a><br>
          <strong>Email:</strong> <a href="mailto:info@chiclanareformas.es">info@chiclanareformas.es</a>
        </div>
      </div>
      <div class="footer-links-block">
        <h4>Servicios</h4>
        <ul>
          <li><a href="reformas-integrales.html">Reformas Integrales</a></li>
          <li><a href="reforma-cocina.html">Reformas de Cocina</a></li>
          <li><a href="reforma-bano.html">Reformas de Baño</a></li>
          <li><a href="construccion-piscinas.html">Piscinas</a></li>
          <li><a href="reforma-terraza-porche.html">Terrazas y Porches</a></li>
          <li><a href="pintura-decoracion.html">Pintura y Decoración</a></li>
        </ul>
      </div>
      <div class="footer-links-block">
        <h4>Empresa</h4>
        <ul>
          <li><a href="sobre-nosotros.html">Sobre Nosotros</a></li>
          <li><a href="contacto.html">Contacto</a></li>
        </ul>
      </div>
      <div class="footer-links-block">
        <h4>Zonas</h4>
        <ul>
          <li><a href="reformas-chiclana-centro.html">Chiclana Centro</a></li>
          <li><a href="reformas-novo-sancti-petri.html">Novo Sancti Petri</a></li>
          <li><a href="reformas-la-barrosa.html">La Barrosa</a></li>
          <li><a href="reformas-pago-del-humo.html">Pago del Humo</a></li>
          <li><a href="reformas-campano.html">Campano</a></li>
        </ul>
        <h4 style="margin-top:18px">Horario</h4>
        <ul>
          <li>Lun–Vie: 8:00 – 20:00</li>
          <li>Sábado: 9:00 – 14:00</li>
        </ul>
      </div>
    </div>
    <div class="site-footer-bottom">
      <p>© 2024 ChiclanaReformas. Todos los derechos reservados.</p>
      <p>Chiclana de la Frontera, Cádiz</p>
    </div>
  </div>
</footer>'''

def faq_schema(questions, answers):
    entities = []
    for q, a in zip(questions, answers):
        entities.append(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}')
    return '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ','.join(entities) + ']}'

for z in ZONES:
    faqs = ""
    for q, a in zip(z["faq_q"], z["faq_a"]):
        faqs += f'''    <div class="faq-item">
      <div class="faq-q">{q} <span class="faq-arrow">▼</span></div>
      <div class="faq-a"><div class="faq-a-inner">{a}</div></div>
    </div>\n'''

    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{z["title_tag"]}</title>
<meta name="description" content="{z["meta_desc"]}">
<link rel="canonical" href="{z["canonical"]}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css?v=1">
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"Service",
  "name":"Reformas en {z['zone']}",
  "description":"Reformas de viviendas en {z['zone']}, Chiclana de la Frontera. Reformas integrales, cocinas, baños, piscinas y más.",
  "provider":{{"@type":"LocalBusiness","name":"ChiclanaReformas","telephone":"856634541","address":{{"@type":"PostalAddress","streetAddress":"Calle de las Flores, 12","addressLocality":"Chiclana de la Frontera","addressRegion":"Cádiz","postalCode":"11130","addressCountry":"ES"}}}},
  "areaServed":{{"@type":"AdministrativeArea","name":"{z['zone']}, Chiclana de la Frontera"}}
}}
</script>
<script type="application/ld+json">
{faq_schema(z["faq_q"], z["faq_a"])}
</script>
</head>
<body>

<header class="topbar">
  <div class="topbar-wrap">
    <a href="/" class="brand">Chiclana<em>Reformas</em></a>
    <nav class="menu-links" id="navMenu">
      <a href="/">Inicio</a>
      <a href="reformas-integrales.html">Reformas Integrales</a>
      <a href="reforma-cocina.html">Cocinas</a>
      <a href="reforma-bano.html">Baños</a>
      <a href="construccion-piscinas.html">Piscinas</a>
      <a href="pintura-decoracion.html">Pintura</a>
      <a href="contacto.html">Contacto</a>
      <a href="sobre-nosotros.html">Nosotros</a>
    </nav>
    <div class="topbar-actions">
      <a href="tel:856634541" class="phonelink"><svg viewBox="0 0 24 24"><path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2a1.003 1.003 0 011.01-.24 11.36 11.36 0 003.58.57 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1 11.36 11.36 0 00.57 3.58 1.003 1.003 0 01-.24 1.01l-2.2 2.2z"/></svg> 856 634 541</a>
      <button class="menu-toggle" id="menuToggle" aria-label="Abrir menú" aria-expanded="false" onclick="toggleMenu()"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>

<div class="breadcrumbs"><a href="/">Inicio</a> <span>›</span> Reformas en {z["zone"]}</div>

<section class="page-hero">
  <div class="page-hero-content">
    <span class="intro-tag">{z["zone_tag"]}</span>
    <h1>Reformas en <span class="hl">{z["h1_span"]}</span></h1>
    <p>{z["lead"]}</p>
  </div>
</section>

<section class="content-zone">
  <div class="content-wrap">
    {z["content"]}
  </div>
</section>

<section class="faq-zone">
  <div class="faq-wrap">
    <div class="faq-zone-head"><h2>Preguntas frecuentes sobre reformas en {z["zone"]}</h2></div>
{faqs}  </div>
</section>

<section class="cta-zone">
  <div class="cta-wrap">
    <h2>¿Necesitas una reforma en {z["zone"]}?</h2>
    <p>Contáctanos para una visita sin compromiso y un presupuesto personalizado.</p>
    <a href="contacto.html" class="cta-btn">Pedir Presupuesto Gratis →</a>
  </div>
</section>

<section class="gmap-zone">
  <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d31687.92!2d-6.17!3d36.42!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd0c33e09988e0f3%3A0x51a3ea86e26e992!2s11130+Chiclana+de+la+Frontera%2C+C%C3%A1diz!5e0!3m2!1ses!2ses!4v1700000000000" allowfullscreen loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa ChiclanaReformas"></iframe>
</section>

{footer()}

<script>
function toggleMenu(){{var m=document.getElementById('navMenu'),t=document.getElementById('menuToggle'),o=m.classList.toggle('open');t.setAttribute('aria-expanded',o);}}
document.querySelectorAll('.faq-q').forEach(function(q){{q.addEventListener('click',function(){{this.parentElement.classList.toggle('open');}});}});
</script>
</body>
</html>'''

    filepath = f'/root/reformaschiclana/{z["slug"]}.html'
    with open(filepath, 'w') as f:
        f.write(html)
    print(f"Created {filepath}")

print("Done!")
