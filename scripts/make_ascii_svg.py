import html
import numpy as np
from PIL import Image

RAMP = " .`:-=+*cs#%@"  # bright (sparse) -> dark (dense)
COLS = 84
ROWS = 45

def make_ascii_svg(input_path="source-prepped.png", output_path="avi-ascii.svg"):
    img = Image.open(input_path).convert("L").resize((COLS, ROWS))
    arr = np.array(img)

    lines = []
    for r in range(ROWS):
        line = ""
        for c in range(COLS):
            val = int(arr[r, c])
            idx = int((255 - val) / 255 * (len(RAMP) - 1))
            line += RAMP[idx]
        lines.append(line)

    width = 370
    height = 430
    line_height = 8.8
    start_y = 24

    defs = []
    body = []

    for i, line in enumerate(lines):
        y = round(start_y + i * line_height, 2)
        delay = round(i * 0.035, 3)
        dur = 0.11
        escaped_line = html.escape(line)

        defs.append(f'''
        <clipPath id="clip-{i}">
          <rect x="12" y="{y - 8}" width="0" height="{line_height + 2}">
            <animate attributeName="width" from="0" to="346" begin="{delay}s" dur="{dur}s" fill="freeze" />
          </rect>
        </clipPath>''')

        body.append(f'''
        <text x="12" y="{y}" clip-path="url(#clip-{i})" xml:space="preserve">{escaped_line}</text>
        <rect x="12" y="{y - 7}" width="5" height="8" fill="#39d353" opacity="0">
          <animate attributeName="x" from="12" to="352" begin="{delay}s" dur="{dur}s" fill="freeze" />
          <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.1;0.9;1" begin="{delay}s" dur="{dur}s" fill="freeze" />
        </rect>''')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
      <style>
        text {{
          font-family: ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace;
          font-size: 6.6px;
          fill: #c9d1d9;
          letter-spacing: 0.15px;
        }}
      </style>
      <rect width="100%" height="100%" rx="10" fill="#0d1117" stroke="#30363d" stroke-width="1"/>
      <defs>{"".join(defs)}</defs>
      {"".join(body)}
    </svg>'''

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    make_ascii_svg()
