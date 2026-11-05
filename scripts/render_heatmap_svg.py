import json
import html

PALETTE = ["#161b22", "#38101C", "#5A1827", "#7D1D3A", "#C77B9B", "#F8F0F3"]

def render_heatmap():
    with open("data/contributions.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    days = data.get("days", [])
    total_text = data.get("total_text", "Contributions in the last year")
    current_streak = data.get("current_streak", 0)
    longest_streak = data.get("longest_streak", 0)

    width = 860
    height = 185
    box_size = 11.5
    gap = 3.5
    start_x = 32
    start_y = 32

    cells = []
    for idx, day in enumerate(days):
        week = idx // 7
        dow = idx % 7
        x = round(start_x + week * (box_size + gap), 2)
        y = round(start_y + dow * (box_size + gap), 2)
        lvl = int(day.get("level", 0))
        # Map level 4 high days to level 5 cream highlight when count is high
        if lvl == 4 and day.get("count", 0) >= 10:
            lvl = 5
        color = PALETTE[min(lvl, len(PALETTE) - 1)]
        delay = round((week + dow) * 0.014, 3)

        cells.append(
            f'<rect class="cell" x="{x}" y="{y}" width="{box_size}" height="{box_size}" '
            f'rx="2.5" fill="{color}" style="animation-delay: {delay}s"/>'
        )

    # Legend (Less -> More)
    legend = []
    lx = width - 165
    ly = height - 28
    legend.append(f'<text x="{lx - 34}" y="{ly + 10}" fill="#C77B9B">Less</text>')
    for i, c in enumerate(PALETTE):
        legend.append(f'<rect x="{lx + i*15}" y="{ly}" width="11" height="11" rx="2.5" fill="{c}"/>')
    legend.append(f'<text x="{lx + 96}" y="{ly + 10}" fill="#C77B9B">More</text>')

    stats_str = f"{total_text}  ·  Current streak: {current_streak}d  ·  Longest: {longest_streak}d"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
      <style>
        text {{
          font-family: ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace;
          font-size: 11.5px;
        }}
        .cell {{
          opacity: 0;
          transform: translateY(-8px);
          animation: dropIn 0.28s ease forwards;
        }}
        @keyframes dropIn {{
          to {{
            opacity: 1;
            transform: translateY(0);
          }}
        }}
      </style>
      <rect width="100%" height="100%" rx="10" fill="#0d1117" stroke="#5A1827" stroke-width="1"/>
      {"".join(cells)}
      <text x="32" y="{height - 18}" fill="#F8F0F3">{html.escape(stats_str)}</text>
      {"".join(legend)}
    </svg>'''

    with open("contrib-heatmap.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated contrib-heatmap.svg")

if __name__ == "__main__":
    render_heatmap()
