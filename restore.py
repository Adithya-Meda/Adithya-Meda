import os
import re

with open("original_build.py", "r", encoding="utf-8") as f:
    build = f.read()

# 1. blueprint_header
build = build.replace('<svg width="800" height="280"', '<svg width="800" height="242"')
build = build.replace('<rect x="20" y="20" width="760" height="240"', '<rect x="20" y="1" width="760" height="240"')
build = build.replace('<rect x="40" y="10" width="{cutout_width}" height="20" fill="{T[\'BG_COLOR\']}"/>', '<rect x="40" y="-8" width="{cutout_width}" height="20" fill="{T[\'BG_COLOR\']}"/>')
build = build.replace('<text x="50" y="25"', '<text x="50" y="7"')
build = build.replace('transform="translate(0, 40)"', 'transform="translate(0, 22)"')

# 2. blueprint_philosophy
build = build.replace('<svg width="800" height="180"', '<svg width="800" height="142"')
build = build.replace('<rect x="20" y="20" width="760" height="140"', '<rect x="20" y="1" width="760" height="140"')
build = build.replace('y="45" font-family="sans-serif"', 'y="26" font-family="sans-serif"')
build = build.replace('transform="translate(40, 80)"', 'transform="translate(40, 61)"')

# 3. blueprint_dns_header
build = build.replace('<svg width="800" height="80"', '<svg width="800" height="50"')
build = build.replace('y="35" font-family="sans-serif"', 'y="15" font-family="sans-serif"')
build = build.replace('y1="50"', 'y1="30"')
build = build.replace('y2="50"', 'y2="30"')
build = build.replace('y="70" font-family="monospace"', 'y="45" font-family="monospace"')

# 4. blueprint_dns_rows
build = build.replace('<svg width="800" height="40"', '<svg width="800" height="36"')
build = build.replace('<rect x="20" y="0" width="760" height="35" fill="{T[\'NODE_BG\']}" fill-opacity="0.6" stroke="{T[\'GRID_COLOR\']}" \nstroke-width="1" rx="6" />', '<rect x="20" y="1" width="760" height="34" fill="{T[\'NODE_BG\']}" stroke="{T[\'LINE_COLOR\']}" stroke-width="1" rx="4" />')
build = build.replace('<rect x="20" y="0" width="760" height="35" fill="{T[\'NODE_BG\']}" fill-opacity="0.6" stroke="{T[\'GRID_COLOR\']}" stroke-width="1" rx="6" />', '<rect x="20" y="1" width="760" height="34" fill="{T[\'NODE_BG\']}" stroke="{T[\'LINE_COLOR\']}" stroke-width="1" rx="4" />')
build = build.replace('cy="17"', 'cy="18"')
build = build.replace('y="22"', 'y="23"')
build = build.replace('y="9"', 'y="10"')

# 5. skills
build = build.replace('<svg width="800" height="180"', '<svg width="800" height="152"')
build = build.replace('y="25" font-family="sans-serif"', 'y="15" font-family="sans-serif"')
build = build.replace('y1="130"', 'y1="110"')
build = build.replace('y2="130"', 'y2="110"')
build = build.replace('130, {x} 130', '110, {x} 110')
build = build.replace('y_offset = 60 if i % 2 == 0 else 90', 'y_offset = 40 if i % 2 == 0 else 70')
build = build.replace('cy="130"', 'cy="110"')

# 6. stats
build = build.replace('<svg width="800" height="200"', '<svg width="800" height="174"')
build = build.replace('<rect x="20" y="10" width="760" height="170"', '<rect x="20" y="2" width="760" height="170"')
build = build.replace('y="35" font-family="sans-serif" font-size="14" fill="{T[\'TEXT_DIM\']}" font-weight="bold" letter-spacing="1">GITHUB STATS', 'y="27" font-family="sans-serif" font-size="14" fill="{T[\'TEXT_DIM\']}" font-weight="bold" letter-spacing="1">GITHUB STATS')
build = build.replace('transform="translate(40, 60)"', 'transform="translate(40, 52)"')
build = build.replace('transform="translate(290, 60)"', 'transform="translate(290, 52)"')
build = build.replace('transform="translate(620, 95)"', 'transform="translate(620, 87)"')


with open("build.py", "w", encoding="utf-8") as f:
    f.write(build)

import os
os.system("python build.py")

import json
# Create exactly stacked README with divs and new cache busters
import build
records = build.CONFIG["dns_records"]
readme = '<div align="center">\n'
def wrap_img(src): return f'<div><img src="{src}" style="display: block; margin: 0; padding: 0; border: none; outline: none; line-height: 0;" /></div>\n'
def wrap_a(href, src): return f'<div><a href="{href}" style="display: block; margin: 0; padding: 0; border: none; outline: none; line-height: 0;"><img src="{src}" style="display: block; margin: 0; padding: 0; border: none; outline: none; line-height: 0;" /></a></div>\n'

readme += wrap_img("./assets/blueprint_header.svg?v=14")
readme += wrap_img("./assets/blueprint_philosophy.svg?v=14")
readme += wrap_img("./assets/blueprint_dns_header.svg?v=14")
for i, r in enumerate(records):
    val = r["value"]
    href = val if val.startswith("http") or val.startswith("mailto") else f"https://{val}"
    readme += wrap_a(href, f"./assets/blueprint_dns_row_{i}.svg?v=14")
readme += wrap_img("./assets/blueprint_skills.svg?v=14")
readme += wrap_img("./assets/blueprint_stats.svg?v=14")

readme += """
<!-- INTERACTIVE DEPLOYMENTS (REPO CARDS) -->
<div style="display: flex; flex-wrap: wrap; justify-content: center; width: 800px; max-width: 100%; margin: 0; padding: 0; line-height: 0;">
  <a href="https://github.com/Adithya-Meda/wisebiz-ecommerce-app" style="display: block; line-height: 0;"><img src="./assets/repo_wisebiz-ecommerce-app.svg?v=14" alt="AWS Landing Zone Resource" style="display: block;"></a>
  <a href="https://github.com/Adithya-Meda/wisebiz-gitops" style="display: block; line-height: 0;"><img src="./assets/repo_wisebiz-gitops.svg?v=14" alt="K8s GitOps Resource" style="display: block;"></a>
  <a href="https://github.com/Adithya-Meda/wisebiz-terraform" style="display: block; line-height: 0;"><img src="./assets/repo_wisebiz-terraform.svg?v=14" alt="Wisebiz Terraform Resource" style="display: block;"></a>
</div>
</div>
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
