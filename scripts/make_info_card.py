import os
import html

HEADER_TITLE = "rasel@deedox"

INFO_ROWS = [
    ("Now", "Founder & Lead Developer @ DEEDOX"),
    ("Agency", "Full-Service AI, Web/App & Media Agency"),
    ("Services", "SaaS, AI Automation & Video Marketing"),
    ("Web", "Next.js, Tailwind CSS, Supabase, Vercel"),
    ("App & AI", "Kotlin, Jetpack Compose, AI Agents"),
    ("Projects", "DEEDOX, Progresso, Screen Time Tracker"),
    ("Location", "Dhaka, Bangladesh"),
]

HIGHLIGHTS = [
    "• Building premium SaaS, web & Android apps at DEEDOX",
    "• Crafting sleek dark-mode & liquid glass UI experiences",
    "• Developing native Android apps with Jetpack Compose",
    "• Automating business workflows with AI agents",
]

def make_info_card(output_path="info-card.svg"):
    static_mode = os.getenv("STATIC", "0") == "1"
    width = 490
    height = 430

    rows_svg = []
    delay = 0.15
    y = 82

    # Header prompt
    rows_svg.append(f'''
    <g class="row" style="animation-delay: 0.05s">
      <text x="24" y="54" fill="#E5B5C7" font-weight="bold" font-size="13.5px">{html.escape(HEADER_TITLE)}</text>
      <text x="24" y="67" fill="#5A1827">----------------------------------------</text>
    </g>''')

    for key, val in INFO_ROWS:
        rows_svg.append(f'''
        <g class="row" style="animation-delay: {delay:.2f}s">
          <text x="24" y="{y}" fill="#C77B9B" font-weight="bold">{html.escape(key)}:</text>
          <text x="108" y="{y}" fill="#F8F0F3">{html.escape(val)}</text>
        </g>''')
        y += 23
        delay += 0.11

    y += 8
    rows_svg.append(f'''
    <g class="row" style="animation-delay: {delay:.2f}s">
      <text x="24" y="{y}" fill="#E5B5C7" font-weight="bold">Highlights</text>
      <text x="24" y="{y + 12}" fill="#5A1827">----------</text>
    </g>''')
    y += 28
    delay += 0.11

    for item in HIGHLIGHTS:
        rows_svg.append(f'''
        <g class="row" style="animation-delay: {delay:.2f}s">
          <text x="24" y="{y}" fill="#D9A5B8">{html.escape(item)}</text>
        </g>''')
        y += 21
        delay += 0.11

    # Brand palette blocks: Deep Burgundy -> Vibrant Wine -> Rose Accent -> Soft Ivory Cream
    colors = ["#3D0C18", "#5A1827", "#701A3D", "#8B2244", "#A32852", "#C77B9B", "#E5B5C7", "#F8F0F3"]
    blocks = "".join([
        f'<rect x="{24 + i*22}" y="{height - 32}" width="16" height="11" rx="2.5" fill="{c}"/>'
        for i, c in enumerate(colors)
    ])
    rows_svg.append(f'<g class="row" style="animation-delay: {delay:.2f}s">{blocks}</g>')

    anim_css = "" if static_mode else '''
        .row {
          opacity: 0;
          transform: translateY(5px);
          animation: fadeIn 0.35s ease forwards;
        }
        @keyframes fadeIn {
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
    '''

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
      <style>
        text {{
          font-family: ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace;
          font-size: 12.2px;
        }}
        {anim_css}
      </style>
      <rect width="100%" height="100%" rx="10" fill="#0d1117" stroke="#5A1827" stroke-width="1"/>
      <circle cx="24" cy="22" r="5.5" fill="#ff5f56"/>
      <circle cx="42" cy="22" r="5.5" fill="#ffbd2e"/>
      <circle cx="60" cy="22" r="5.5" fill="#27c93f"/>
      <text x="245" y="26" fill="#C77B9B" font-size="11px" text-anchor="middle">rasel@deedox: ~ (neofetch)</text>
      {"".join(rows_svg)}
    </svg>'''

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    make_info_card()
