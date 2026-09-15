from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]

# Homepage
index = root / "index.html"
text = index.read_text(encoding="utf-8")
text = text.replace('<small>Products</small><b>5</b>', '<small>Products</small><b>6</b>')
text = text.replace(
    'Developer behind DOBERTO FLIX, AYITI MARKET, DOBERTO MD V3, DOBERTO VCF and NOVATOP.',
    'Developer behind DOBERTO FLIX, AYITI MARKET, DOBERTO MD V3, DOBERTO VCF, DOBERTO MINI MD and NOVATOP.'
)
text = text.replace('assets/portfolio-ui.js?v=20260912-pro2', 'assets/portfolio-ui.js?v=20260915-auto1')

card = '''
<article class="project reveal" style="--accent:#25d366"><div class="product-mark"><img src="https://doberto-minibot-v1.vercel.app/bot-logo-v4.svg" width="82" height="82" alt="DOBERTO MINI MD icon" decoding="async" data-fallback="DM"></div><div class="project-main"><div class="project-title-row"><h3>DOBERTO MINI MD</h3><span class="live"><span class="live-dot"></span>Live</span><span class="source-private">Private source</span><span class="domain">doberto-minibot-v1.vercel.app</span></div><p>Multi-session WhatsApp automation bot with pairing, session management and practical command workflows.</p><div class="chips"><span class="chip">Automation</span><span class="chip">Pairing</span><span class="chip">Multi-session</span><span class="chip">WhatsApp</span></div></div><div class="project-actions"><a class="primary" href="https://doberto-minibot-v1.vercel.app" target="_blank" rel="noopener">Open live<span class="icon"><svg viewBox="0 0 24 24"><path d="M7 17L17 7"/><path d="M8 7h9v9"/></svg></span></a><a href="case-studies/doberto-mini-md.html">Case study<span class="icon"><svg viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg></span></a></div></article>'''
marker = '\n</div></div></section>\n\n<section id="stack">'
if 'DOBERTO MINI MD</h3>' not in text:
    if marker not in text:
        raise RuntimeError('Project-list insertion marker not found')
    text = text.replace(marker, card + marker, 1)
index.write_text(text, encoding="utf-8")

# Homepage translations
pui = root / "assets/portfolio-ui.js"
js = pui.read_text(encoding="utf-8")
en_old = "{desc:'Contact utility platform built around VCF workflows, WhatsApp communities and visibility tools.',chips:['Utility','Contacts','WhatsApp','Community']}"
en_new = en_old + ",\n    {desc:'Multi-session WhatsApp automation bot with pairing, session management and practical command workflows.',chips:['Automation','Pairing','Multi-session','WhatsApp']}"
fr_old = "{desc:'Plateforme utilitaire autour des fichiers VCF, des communautés WhatsApp et des outils de visibilité.',chips:['Utilitaire','Contacts','WhatsApp','Communauté']}"
fr_new = fr_old + ",\n    {desc:'Bot d’automatisation WhatsApp multi-session avec appairage, gestion des sessions et commandes pratiques.',chips:['Automatisation','Appairage','Multi-session','WhatsApp']}"
if 'Multi-session WhatsApp automation bot with pairing' not in js:
    if en_old not in js or fr_old not in js:
        raise RuntimeError('Portfolio translation insertion point not found')
    js = js.replace(en_old, en_new, 1).replace(fr_old, fr_new, 1)
pui.write_text(js, encoding="utf-8")

# Case-study translations
cui = root / "assets/case-ui.js"
cjs = cui.read_text(encoding="utf-8")
mini_entry = "'DOBERTO MINI MD':{en:{lead:'Multi-session WhatsApp automation bot with a professional pairing website, session management and command workflows.',product:'Make pairing and multi-session bot access simple while keeping session state, commands and deployment practical to manage.',build:'I built the pairing website, multi-session flow, session controls, command system and deployment structure around an always-on bot worker.',chips:['Automation','WhatsApp','Pairing','Multi-session','Commands'],meta:'doberto-minibot-v1.vercel.app · Automation'},fr:{lead:'Bot d’automatisation WhatsApp multi-session avec site d’appairage professionnel, gestion des sessions et workflows de commandes.',product:'Simplifier l’appairage et l’accès multi-session tout en gardant les sessions, les commandes et le déploiement faciles à gérer.',build:'J’ai construit le site d’appairage, le flux multi-session, les contrôles de session, le système de commandes et la structure de déploiement autour d’un worker toujours actif.',chips:['Automatisation','WhatsApp','Appairage','Multi-session','Commandes'],meta:'doberto-minibot-v1.vercel.app · Automatisation'}}"
if "'DOBERTO MINI MD':" not in cjs:
    needle = "meta:'dobertovcf.online · Utilitaire'}}};\nlet lang="
    replacement = "meta:'dobertovcf.online · Utilitaire'}},\n" + mini_entry + "};\nlet lang="
    if needle not in cjs:
        raise RuntimeError('Case-study translation insertion point not found')
    cjs = cjs.replace(needle, replacement, 1)
cui.write_text(cjs, encoding="utf-8")

# Case-study page
case = root / "case-studies/doberto-mini-md.html"
case.write_text('''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>DOBERTO MINI MD Case Study | DOBERTO MRLIT DEV</title>
<meta name="description" content="DOBERTO MINI MD is a multi-session WhatsApp automation product developed by DOBERTO MRLIT DEV with pairing, sessions and command workflows.">
<meta name="robots" content="index,follow,max-image-preview:large"><meta name="theme-color" content="#07090d"><meta name="color-scheme" content="dark light">
<link rel="canonical" href="https://dobertomrlit.zone.id/case-studies/doberto-mini-md.html"><link rel="icon" href="../favicon.svg" type="image/svg+xml"><script>try{const t=localStorage.getItem('doberto-theme');document.documentElement.dataset.theme=t||(matchMedia('(prefers-color-scheme: light)').matches?'light':'dark')}catch(_){document.documentElement.dataset.theme='dark'}</script><link rel="stylesheet" href="../assets/case-study.css?v=20260912-pro2"><link rel="stylesheet" href="../assets/case-preferences.css?v=20260905-cinematic1"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<meta property="og:type" content="article"><meta property="og:site_name" content="DOBERTO MRLIT DEV"><meta property="og:title" content="DOBERTO MINI MD Case Study"><meta property="og:description" content="Multi-session WhatsApp automation with pairing, sessions and command workflows."><meta property="og:url" content="https://dobertomrlit.zone.id/case-studies/doberto-mini-md.html"><meta property="og:image" content="https://dobertomrlit.zone.id/assets/og-preview-v2.jpg?v=20260905-final"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="https://dobertomrlit.zone.id/assets/og-preview-v2.jpg?v=20260905-final">
<script type="application/ld+json">{"@context":"https://schema.org","@graph":[{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Portfolio","item":"https://dobertomrlit.zone.id/"},{"@type":"ListItem","position":2,"name":"DOBERTO MINI MD","item":"https://dobertomrlit.zone.id/case-studies/doberto-mini-md.html"}]},{"@type":"SoftwareApplication","name":"DOBERTO MINI MD","url":"https://doberto-minibot-v1.vercel.app","applicationCategory":"UtilitiesApplication","creator":{"@type":"Person","name":"DOBERTO MRLIT DEV","url":"https://dobertomrlit.zone.id/"}}]}</script>
</head>
<body style="--accent:#25d366">
<header class="top"><div class="w topin"><a class="back" href="../index.html#work"><span class="icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg></span><span>Portfolio</span></a><a class="live" href="https://doberto-minibot-v1.vercel.app" target="_blank" rel="noopener"><span class="label">Open live</span><span class="icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17L17 7"/><path d="M8 7h9v9"/></svg></span></a></div></header>
<main><section class="hero"><div class="w"><nav class="crumbs" aria-label="Breadcrumb"><a href="../index.html">Portfolio</a><span class="icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg></span><span>DOBERTO MINI MD</span></nav><div class="kicker">Product Case Study</div><h1>DOBERTO MINI MD</h1><p class="lead">Multi-session WhatsApp automation bot with a professional pairing website, session management and command workflows.</p><div class="identity"><div class="identity-icon"><img src="https://doberto-minibot-v1.vercel.app/bot-logo-v4.svg" width="72" height="72" alt="DOBERTO MINI MD icon"></div><div class="identity-copy"><small>Official product · Private source</small><strong>DOBERTO MINI MD</strong><span>doberto-minibot-v1.vercel.app · Automation</span></div><div class="identity-status"><span class="status-dot"></span>Live</div></div></div></section><section><div class="w"><div class="grid"><article class="box"><h2>Problem</h2><p>Make pairing and multi-session bot access simple while keeping session state, commands and deployment practical to manage.</p></article><article class="box"><h2>Solution</h2><p>I built the pairing website, multi-session flow, session controls, command system and deployment structure around an always-on bot worker.</p></article><article class="box"><h2>Core features</h2><div class="stack"><span class="chip">Automation</span><span class="chip">WhatsApp</span><span class="chip">Pairing</span><span class="chip">Multi-session</span><span class="chip">Commands</span></div></article><article class="box"><h2>Status</h2><p>Live product under active development and maintenance.</p></article></div><div class="bottom"><a class="btn primary" href="https://doberto-minibot-v1.vercel.app" target="_blank" rel="noopener">Open live project<span class="icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17L17 7"/><path d="M8 7h9v9"/></svg></span></a><a class="btn" href="../index.html#work">Back to projects<span class="icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg></span></a></div></div></section></main>
<footer class="footer"><div class="w foot"><span>DOBERTO MRLIT DEV</span><span>© 2026</span></div></footer>
<script src="../assets/case-ui.js?v=20260915-auto1"></script>
</body></html>''', encoding="utf-8")

# Sitemap
sitemap = root / "sitemap.xml"
sm = sitemap.read_text(encoding="utf-8")
sm = sm.replace('<url><loc>https://dobertomrlit.zone.id/</loc><lastmod>2026-09-05</lastmod>', '<url><loc>https://dobertomrlit.zone.id/</loc><lastmod>2026-09-15</lastmod>')
mini_url = '  <url><loc>https://dobertomrlit.zone.id/case-studies/doberto-mini-md.html</loc><lastmod>2026-09-15</lastmod><priority>0.8</priority></url>\n'
if 'case-studies/doberto-mini-md.html' not in sm:
    sm = sm.replace('</urlset>', mini_url + '</urlset>')
sitemap.write_text(sm, encoding="utf-8")

# Baseline for future automatic sync: existing repositories are considered seen.
registry = {
    "version": 1,
    "baseline_at": "2026-09-15",
    "auto_add_new_repositories": True,
    "owner": "Doberto555",
    "portfolio_repository": "Doberto555/Doberto555",
    "seen_repositories": [
        "Doberto555/QUEEN-VALENTINA-MD",
        "Doberto555/DOBERTO-XD-V2",
        "Doberto555/DOBERTO-FLIX",
        "Doberto555/DOBERTO-VCF",
        "Doberto555/DOBERTO-MD-V3",
        "Doberto555/DOBERTO-EARN",
        "Doberto555/NOVATOP",
        "Doberto555/Doberto555",
        "Doberto555/DOBERTO-APK",
        "Doberto555/MINIT-PAY",
        "Doberto555/DOBERTO-MINI-BOT-V1"
    ],
    "portfolio_projects": [
        "Doberto555/DOBERTO-FLIX",
        "AYITI MARKET",
        "Doberto555/DOBERTO-MD-V3",
        "Doberto555/DOBERTO-VCF",
        "Doberto555/NOVATOP",
        "Doberto555/DOBERTO-MINI-BOT-V1"
    ],
    "rules": {
        "ignore_archived": True,
        "ignore_forks": True,
        "ignore_portfolio_repo": True,
        "new_repositories_only_after_baseline": True,
        "prefer_production_domain_over_vercel_preview": True
    }
}
(root / "assets/project-sync.json").write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")

print('DOBERTO MINI MD portfolio update prepared successfully.')
