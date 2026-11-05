import os

os.makedirs("assets", exist_ok=True)

# 1. Animated Hero Banner (assets/hero-banner.svg) - Burgundy & Cream Theme
hero_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="170" viewBox="0 0 860 170">
  <defs>
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1117"/>
      <stop offset="50%" stop-color="#1c0b13"/>
      <stop offset="100%" stop-color="#0d1117"/>
    </linearGradient>
    <linearGradient id="neon-line" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0d1117" stop-opacity="0"/>
      <stop offset="25%" stop-color="#701A3D" stop-opacity="1"/>
      <stop offset="50%" stop-color="#E5B5C7" stop-opacity="1"/>
      <stop offset="75%" stop-color="#5A1827" stop-opacity="1"/>
      <stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>
    </linearGradient>
    <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#2a121b" stroke-width="0.7"/>
    </pattern>
  </defs>
  <rect width="860" height="170" rx="10" fill="url(#bg-grad)" stroke="#5A1827" stroke-width="1"/>
  <rect width="860" height="170" rx="10" fill="url(#grid)" opacity="0.6"/>

  <!-- Animated Orbital / Terminal Pulse Geometry -->
  <circle cx="780" cy="85" r="45" fill="none" stroke="#701A3D" stroke-width="1" stroke-dasharray="6 4" opacity="0.5">
    <animateTransform attributeName="transform" type="rotate" from="0 780 85" to="360 780 85" dur="18s" repeatCount="indefinite"/>
  </circle>
  <circle cx="780" cy="85" r="28" fill="none" stroke="#C77B9B" stroke-width="1" stroke-dasharray="4 6" opacity="0.6">
    <animateTransform attributeName="transform" type="rotate" from="360 780 85" to="0 780 85" dur="12s" repeatCount="indefinite"/>
  </circle>
  <circle cx="780" cy="85" r="4" fill="#E5B5C7">
    <animate attributeName="opacity" values="0.3;1;0.3" dur="2s" repeatCount="indefinite"/>
  </circle>

  <!-- Window Controls -->
  <circle cx="24" cy="22" r="5.5" fill="#ff5f56"/>
  <circle cx="42" cy="22" r="5.5" fill="#ffbd2e"/>
  <circle cx="60" cy="22" r="5.5" fill="#27c93f"/>
  <text x="82" y="26" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="11" fill="#C77B9B">rasel@deedox: ~/identity.sh</text>

  <!-- Main Identity Typography -->
  <text x="36" y="78" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="28" font-weight="bold" fill="#F8F0F3" letter-spacing="1">RASEL AHMED <tspan fill="#E5B5C7">// DEEDOX</tspan></text>
  <text x="36" y="108" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="13.5" fill="#C77B9B">Founder &amp; Lead Developer  ·  Full-Stack Web, Android &amp; AI Automation Agency</text>
  <text x="36" y="132" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="12" fill="#D9A5B8">Building scalable SaaS platforms, native Jetpack Compose apps &amp; intelligent workflows.</text>

  <!-- Glowing Animated Underline -->
  <rect x="36" y="148" width="420" height="2" fill="url(#neon-line)">
    <animate attributeName="x" values="36;280;36" dur="6s" repeatCount="indefinite"/>
  </rect>
</svg>'''

with open("assets/hero-banner.svg", "w", encoding="utf-8") as f:
    f.write(hero_svg)

# 2. Featured Projects & Agency Showcase (assets/projects-showcase.svg) - Burgundy & Cream Theme
projects_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="210" viewBox="0 0 860 210">
  <style>
    .title { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 14px; font-weight: bold; fill: #E5B5C7; }
    .sub { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 11.5px; fill: #F8F0F3; }
    .muted { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 11px; fill: #D9A5B8; }
    .tag { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 10.5px; fill: #C77B9B; }
    .card { opacity: 0; animation: fadeUp 0.4s ease forwards; }
    @keyframes fadeUp { to { opacity: 1; } }
  </style>

  <!-- Card 1: DEEDOX -->
  <g class="card" style="animation-delay: 0.1s">
    <rect x="0" y="0" width="276" height="205" rx="10" fill="#0d1117" stroke="#5A1827" stroke-width="1"/>
    <rect x="0" y="0" width="276" height="4" rx="2" fill="#701A3D"/>
    <text x="18" y="32" class="title">01 // DEEDOX PLATFORM</text>
    <text x="18" y="56" class="sub">AI Startup &amp; Digital Agency</text>
    <text x="18" y="80" class="muted">Full-service agency delivering</text>
    <text x="18" y="96" class="muted">premium websites, SaaS products,</text>
    <text x="18" y="112" class="muted">AI automation &amp; video marketing.</text>
    <rect x="18" y="138" width="240" height="1" fill="#38141F"/>
    <text x="18" y="162" class="tag">Next.js · Tailwind · Supabase</text>
    <text x="18" y="182" class="tag">AI Agents · Vercel · UI/UX</text>
  </g>

  <!-- Card 2: PROGRESSO -->
  <g class="card" style="animation-delay: 0.25s">
    <rect x="292" y="0" width="276" height="205" rx="10" fill="#0d1117" stroke="#5A1827" stroke-width="1"/>
    <rect x="292" y="0" width="276" height="4" rx="2" fill="#C77B9B"/>
    <text x="310" y="32" class="title">02 // PROGRESSO APP</text>
    <text x="310" y="56" class="sub">Minimalist Productivity OS</text>
    <text x="310" y="80" class="muted">Native Android habit tracker,</text>
    <text x="310" y="96" class="muted">routine builder, discipline stats</text>
    <text x="310" y="112" class="muted">&amp; background app blocker.</text>
    <rect x="310" y="138" width="240" height="1" fill="#38141F"/>
    <text x="310" y="162" class="tag">Kotlin · Jetpack Compose</text>
    <text x="310" y="182" class="tag">Android SDK · Material 3</text>
  </g>

  <!-- Card 3: SCREEN TIME TRACKER -->
  <g class="card" style="animation-delay: 0.4s">
    <rect x="584" y="0" width="276" height="205" rx="10" fill="#0d1117" stroke="#5A1827" stroke-width="1"/>
    <rect x="584" y="0" width="276" height="4" rx="2" fill="#E5B5C7"/>
    <text x="602" y="32" class="title">03 // SCREEN TIME SYNC</text>
    <text x="602" y="56" class="sub">Cloud Usage Analytics</text>
    <text x="602" y="80" class="muted">Long-term Android screen time</text>
    <text x="602" y="96" class="muted">backup engine syncing daily device</text>
    <text x="602" y="112" class="muted">metrics to a live web dashboard.</text>
    <rect x="602" y="138" width="240" height="1" fill="#38141F"/>
    <text x="602" y="162" class="tag">WorkManager · UsageStatsManager</text>
    <text x="602" y="182" class="tag">Supabase · Jetpack Compose</text>
  </g>
</svg>'''

with open("assets/projects-showcase.svg", "w", encoding="utf-8") as f:
    f.write(projects_svg)

# 3. Categorized Tech Stack & Capabilities Matrix (assets/skills-matrix.svg) - Burgundy & Cream Theme
skills_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="190" viewBox="0 0 860 190">
  <style>
    text { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 12px; }
    .cat { fill: #E5B5C7; font-weight: bold; }
    .val { fill: #F8F0F3; }
  </style>
  <rect width="860" height="190" rx="10" fill="#0d1117" stroke="#5A1827" stroke-width="1"/>
  <circle cx="24" cy="22" r="5.5" fill="#ff5f56"/>
  <circle cx="42" cy="22" r="5.5" fill="#ffbd2e"/>
  <circle cx="60" cy="22" r="5.5" fill="#27c93f"/>
  <text x="430" y="25" fill="#C77B9B" font-size="11px" text-anchor="middle">rasel@deedox: ~/capabilities --list</text>

  <text x="28" y="58" class="cat">[Web &amp; SaaS]</text>
  <text x="190" y="58" class="val">Next.js · React · Tailwind CSS · TypeScript · Supabase · Vercel</text>

  <text x="28" y="88" class="cat">[Android Native]</text>
  <text x="190" y="88" class="val">Kotlin · Jetpack Compose · WorkManager · Material UI · Web-to-APK</text>

  <text x="28" y="118" class="cat">[AI &amp; Automation]</text>
  <text x="190" y="118" class="val">AI Agents · OpenRouter API · Business Chatbots · Workflow Automation</text>

  <text x="28" y="148" class="cat">[Agency &amp; Design]</text>
  <text x="190" y="148" class="val">Dark-Mode &amp; Liquid Glass UI · Brand Identity · AI Video Marketing</text>

  <text x="28" y="174" fill="#C77B9B" font-size="11px">status: all systems operational  ·  focus: shipping high-craft digital products</text>
</svg>'''

with open("assets/skills-matrix.svg", "w", encoding="utf-8") as f:
    f.write(skills_svg)

# 4. Minimal Animated Footer (assets/footer-wave.svg) - Burgundy & Cream Theme
footer_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="54" viewBox="0 0 860 54">
  <rect width="860" height="54" rx="10" fill="#0d1117" stroke="#5A1827" stroke-width="1"/>
  <circle cx="28" cy="27" r="4.5" fill="#E5B5C7">
    <animate attributeName="opacity" values="1;0.2;1" dur="1.8s" repeatCount="indefinite"/>
  </circle>
  <text x="44" y="31" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="12" fill="#F8F0F3">
    rasel@deedox ~ $ echo "Create with intention. Ship with care."
  </text>
  <text x="832" y="31" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="11" fill="#E5B5C7" text-anchor="end">
    [EOF]
  </text>
</svg>'''

with open("assets/footer-wave.svg", "w", encoding="utf-8") as f:
    f.write(footer_svg)

print("Successfully generated all 4 extra SVG assets in assets/ with Burgundy & Cream theme")
