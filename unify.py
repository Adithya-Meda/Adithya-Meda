import os
import re

with open("original_build.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.startswith("def generate_blueprint_header():"):
        break
    new_lines.append(line)

new_build_py = "".join(new_lines)

# Now we append the unified layout function and the original repo card function
new_build_py += """
def generate_blueprint_main():
    import html
    
    p = CONFIG["profile"]
    phil = CONFIG["philosophy"]
    skills = CONFIG["skills"]
    stats = CONFIG["stats"]
    
    username = p.get("github_username", "")
    if username:
        real = fetch_github_stats(username)
        if real:
            stats['commits'] = real['commits']
            stats['prs'] = real['prs']
            stats['issues'] = real['issues']
            
    subtitle_escaped = html.escape(p.get("subtitle", ""))
    automation_escaped = html.escape(phil.get("automation", ""))
    security_escaped = html.escape(phil.get("security", ""))
    title_escaped = html.escape(p.get("title", ""))
    region_text = f"REGION: {p.get('region', 'GLOBAL')}"
    
    cutout_width = len(region_text) * 8 + 40
    
    svg = f'''<svg width="800" height="840" xmlns="http://www.w3.org/2000/svg">
  {defs_premium()}
  
  <!-- ================= HEADER (0 - 280) ================= -->
  <g transform="translate(0, 0)">
    <rect x="20" y="20" width="760" height="240" fill="none" stroke="{T['TEXT_DIM']}" stroke-width="1" stroke-dasharray="10,5" rx="12"/>
    <rect x="40" y="10" width="{cutout_width}" height="20" fill="{T['BG_COLOR']}"/>
    <text x="50" y="25" font-family="sans-serif" font-size="12" fill="{T['TEXT_DIM']}" font-weight="bold">{region_text}</text>
    
    <g transform="translate(0, 40)">
      <path id="data-path" d="M 180 50 C 220 50, 220 110, 270 110" fill="none" stroke="{T['LINE_COLOR']}" stroke-width="2" stroke-dasharray="4,4"/>
      <circle cx="210" cy="80" r="4" fill="#ffffff" filter="url(#drop-shadow)"/>
      
      <g transform="translate(40, 20)" filter="url(#drop-shadow)">
        <rect width="140" height="70" fill="{T['NODE_BG']}" stroke="{T['LINE_COLOR']}" stroke-width="1" rx="8"/>
        <circle cx="20" cy="20" r="6" fill="none" stroke="{T['LINE_COLOR']}" stroke-width="2"/>
        <circle cx="20" cy="20" r="2" fill="{T['LINE_COLOR']}"/>
        <text x="40" y="23" font-family="sans-serif" font-size="10" fill="{T['TEXT_DIM']}">INGRESS ROUTER</text>
        <text x="40" y="41" font-family="monospace" font-size="14" fill="{T['TEXT_MAIN']}" font-weight="bold">App ALB</text>
      </g>
      
      <g transform="translate(270, 40)" filter="url(#drop-shadow)">
        <rect width="320" height="120" fill="{T['NODE_BG']}" stroke="{T['LINE_COLOR']}" stroke-width="2" rx="8"/>
        <circle cx="20" cy="20" r="4" fill="#FF5F56"/>
        <circle cx="35" cy="20" r="4" fill="#FFBD2E"/>
        <circle cx="50" cy="20" r="4" fill="#27C93F"/>
        <text x="160" y="55" font-family="sans-serif" font-size="28" fill="{T['TEXT_MAIN']}" font-weight="bold" text-anchor="middle">{p.get("github_username", "")}</text>
        <text x="160" y="85" font-family="monospace" font-size="14" fill="{T['LINE_COLOR']}" font-weight="bold" text-anchor="middle">{subtitle_escaped}</text>
        <circle cx="160" cy="120" r="10" fill="{T['LINE_COLOR']}" opacity="0.3"/>
        <circle cx="160" cy="120" r="5" fill="{T['LINE_COLOR']}"/>
      </g>
      
      <path id="data-path-out" d="M 590 110 C 640 110, 640 50, 680 50" fill="none" stroke="{T['LINE_COLOR']}" stroke-width="2" stroke-dasharray="4,4"/>
      <circle cx="615" cy="80" r="4" fill="#ffffff" filter="url(#drop-shadow)"/>
      <g transform="translate(670, 30)" filter="url(#drop-shadow)">
        <path d="M 0 20 Q 40 0 80 20 L 80 60 Q 40 80 0 60 Z" fill="{T['NODE_BG']}" stroke="{T['LINE_COLOR']}" stroke-width="1"/>
        <path d="M 0 20 Q 40 40 80 20" fill="none" stroke="{T['LINE_COLOR']}" stroke-width="1"/>
        <text x="40" y="45" font-family="monospace" font-size="12" fill="{T['TEXT_MAIN']}" font-weight="bold" text-anchor="middle">Brain.db</text>
      </g>
    </g>
  </g>

  <!-- ================= PHILOSOPHY (280 - 460) ================= -->
  <g transform="translate(0, 280)">
    <rect x="20" y="20" width="760" height="140" fill="{T['NODE_BG']}" fill-opacity="0.8" stroke="{T['GRID_COLOR']}" stroke-width="1" rx="8"/>
    <text x="40" y="45" font-family="sans-serif" font-size="12" fill="{T['TEXT_DIM']}" font-weight="bold" letter-spacing="1">CONFIGMAP: ENGINEERING_PHILOSOPHY.YAML</text>
    <g font-family="monospace" font-size="14" fill="{T['TEXT_MAIN']}" transform="translate(40, 80)">
      <text y="0"><tspan fill="#FFBD2E">apiVersion:</tspan> v1</text>
      <text y="20"><tspan fill="#FFBD2E">kind:</tspan> CoreValues</text>
      <text y="40"><tspan fill="#FFBD2E">data:</tspan></text>
      <text y="60">  <tspan fill="{T['LINE_COLOR']}">automation:</tspan> "{automation_escaped}"</text>
      <text y="80">  <tspan fill="{T['LINE_COLOR']}">security:</tspan> "{security_escaped}"</text>
    </g>
  </g>

  <!-- ================= SKILLS (460 - 640) ================= -->
  <g transform="translate(0, 460)">
    <text x="400" y="25" font-family="sans-serif" font-size="12" fill="{T['TEXT_DIM']}" font-weight="bold" letter-spacing="2" text-anchor="middle">TECH STACK TOPOLOGY (SUBNETS)</text>
    <line x1="100" y1="130" x2="700" y2="130" stroke="{T['TEXT_DIM']}" stroke-width="2" stroke-dasharray="5,5"/>
'''
    for i, (name, x) in enumerate(skills):
        y_offset = 60 if i % 2 == 0 else 90
        svg += f'''
    <path d="M {x} {y_offset+15} C {x} {y_offset+30}, {x} 130, {x} 130" fill="none" stroke="{T['LINE_COLOR']}" stroke-width="2"/>
    <circle cx="{x}" cy="130" r="4" fill="{T['LINE_COLOR']}">
      <animate attributeName="opacity" values="1;0.2;1" dur="{1.5 + i*0.3}s" repeatCount="indefinite"/>
    </circle>
    <g transform="translate({x-50}, {y_offset-15})" filter="url(#drop-shadow)">
      <rect width="100" height="30" fill="{T['NODE_BG']}" stroke="{T['LINE_COLOR']}" stroke-width="1" rx="15">
        <animate attributeName="stroke-width" values="1;3;1" dur="{1.5 + i*0.3}s" repeatCount="indefinite"/>
        <animate attributeName="stroke" values="{T['LINE_COLOR']};#ffffff;{T['LINE_COLOR']}" dur="{1.5 + i*0.3}s" repeatCount="indefinite"/>
      </rect>
      <text x="50" y="20" font-family="monospace" font-size="12" fill="{T['TEXT_MAIN']}" font-weight="bold" text-anchor="middle">{name}</text>
    </g>'''

    svg += f'''
  </g>

  <!-- ================= STATS (640 - 840) ================= -->
  <g transform="translate(0, 640)">
    <rect x="20" y="10" width="760" height="170" fill="{T['NODE_BG']}" stroke="{T['GRID_COLOR']}" stroke-width="2" rx="12" filter="url(#drop-shadow)"/>
    <text x="40" y="35" font-family="sans-serif" font-size="14" fill="{T['TEXT_DIM']}" font-weight="bold" letter-spacing="1">GITHUB STATS</text>
    
    <g transform="translate(40, 60)">
      <text x="0" y="10" font-family="sans-serif" font-size="12" fill="{T['TEXT_DIM']}">Total Commits</text>
      <text x="0" y="45" font-family="monospace" font-size="32" fill="{T['TEXT_MAIN']}" font-weight="bold">{stats['commits']}</text>
      <path d="M 120 40 C 135 40, 140 20, 155 20 C 170 20, 175 10, 190 10 C 205 10, 210 30, 225 30 L 225 50 L 120 50 Z" fill="url(#chart-grad)"/>
      <path d="M 120 40 C 135 40, 140 20, 155 20 C 170 20, 175 10, 190 10 C 205 10, 210 30, 225 30" fill="none" stroke="{T['LINE_COLOR']}" stroke-width="2"/>
    </g>
    
    <g transform="translate(290, 60)">
      <text x="0" y="10" font-family="sans-serif" font-size="12" fill="{T['TEXT_DIM']}">Total PRs</text>
      <text x="0" y="45" font-family="monospace" font-size="32" fill="{T['TEXT_MAIN']}" font-weight="bold">{stats['prs']}</text>
      <path d="M 140 30 C 155 30, 160 40, 175 40 C 190 40, 195 10, 210 10 C 225 10, 230 20, 245 20 L 245 50 L 140 50 Z" fill="url(#chart-grad)"/>
      <path d="M 140 30 C 155 30, 160 40, 175 40 C 190 40, 195 10, 210 10 C 225 10, 230 20, 245 20" fill="none" stroke="{T['LINE_COLOR']}" stroke-width="2"/>
    </g>
    
    <g transform="translate(620, 95)">
      <circle cx="0" cy="0" r="30" fill="none" stroke="{T['GRID_COLOR']}" stroke-width="6"/>
      <circle cx="0" cy="0" r="30" fill="none" stroke="{T['LINE_COLOR']}" stroke-width="6" stroke-dasharray="188" stroke-dashoffset="40" stroke-linecap="round"/>
      <text x="0" y="5" font-family="monospace" font-size="20" fill="{T['TEXT_MAIN']}" font-weight="bold" text-anchor="middle">{stats['issues']}</text>
      <text x="0" y="50" font-family="sans-serif" font-size="12" fill="{T['TEXT_DIM']}" text-anchor="middle">Total Issues</text>
    </g>
  </g>

</svg>'''
    
    write_svg("blueprint_main.svg", svg)

def fetch_github_stats(username):
    headers = {'User-Agent': 'Mozilla/5.0'}
    stats = {"commits": 0, "prs": 0, "issues": 0}
    try:
        req = urllib.request.Request(f"https://api.github.com/search/commits?q=author:{username}", headers={**headers, 'Accept': 'application/vnd.github.cloak-preview'})
        with urllib.request.urlopen(req) as response:
            import json
            stats["commits"] = json.loads(response.read().decode()).get("total_count", 0)
        req = urllib.request.Request(f"https://api.github.com/search/issues?q=author:{username}+type:pr", headers=headers)
        with urllib.request.urlopen(req) as response:
            import json
            stats["prs"] = json.loads(response.read().decode()).get("total_count", 0)
        req = urllib.request.Request(f"https://api.github.com/search/issues?q=author:{username}+type:issue", headers=headers)
        with urllib.request.urlopen(req) as response:
            import json
            stats["issues"] = json.loads(response.read().decode()).get("total_count", 0)
        return stats
    except Exception as e:
        return None

def generate_repo_blueprint(name, desc, is_centered_wide=False):
    filename = name.replace(" ", "_").lower()
    width = 800 if is_centered_wide else 400
    offset_x = 200 if is_centered_wide else 0
    svg = f'''<svg width="{width}" height="140" xmlns="http://www.w3.org/2000/svg">
  {defs_premium()}
  <rect x="{15 + offset_x}" y="10" width="370" height="120" fill="{T['NODE_BG']}" fill-opacity="0.9" stroke="{T['GRID_COLOR']}" stroke-width="2" rx="10" filter="url(#drop-shadow)"/>
  <circle cx="{45 + offset_x}" cy="40" r="16" fill="none" stroke="{T['LINE_COLOR']}" stroke-width="2"/>
  <circle cx="{45 + offset_x}" cy="40" r="6" fill="{T['LINE_COLOR']}" filter="url(#neon-glow)"/>
  <text x="{75 + offset_x}" y="45" font-family="monospace" font-size="18" fill="{T['TEXT_MAIN']}" font-weight="bold">{name}</text>
  <text x="{35 + offset_x}" y="80" font-family="sans-serif" font-size="13" fill="{T['TEXT_DIM']}">{desc}</text>
  <rect x="{35 + offset_x}" y="100" width="10" height="10" fill="{T['LINE_COLOR']}" rx="2"/>
  <text x="{55 + offset_x}" y="110" font-family="monospace" font-size="11" fill="{T['LINE_COLOR']}" letter-spacing="1">ACTIVE DEPLOYMENT</text>
  <style>rect:hover {{ stroke: {T['LINE_COLOR']}; }}</style>
</svg>'''
    write_svg(f"repo_{filename}.svg", svg)

if __name__ == "__main__":
    generate_blueprint_main()
    repos = CONFIG["repos"]
    for i, repo in enumerate(repos):
        is_last = (i == len(repos) - 1)
        is_odd_total = (len(repos) % 2 != 0)
        is_centered_wide = (is_last and is_odd_total)
        generate_repo_blueprint(repo['name'], repo['desc'], is_centered_wide)
    print("Generated unified main SVG and repo cards!")
"""

with open("build.py", "w", encoding="utf-8") as f:
    f.write(new_build_py)

import os
os.system("python build.py")

readme = '<div align="center">\n'
readme += '<img src="./assets/blueprint_main.svg?v=15" style="display: block; margin: 0; padding: 0; border: none; outline: none;" />\n'
readme += """
<!-- INTERACTIVE DEPLOYMENTS (REPO CARDS) -->
<div style="display: flex; flex-wrap: wrap; justify-content: center; width: 800px; max-width: 100%; margin: 0; padding: 0;">
  <a href="https://github.com/Adithya-Meda/wisebiz-ecommerce-app" style="display: block;"><img src="./assets/repo_wisebiz-ecommerce-app.svg?v=15" alt="AWS Landing Zone Resource" style="display: block;"></a>
  <a href="https://github.com/Adithya-Meda/wisebiz-gitops" style="display: block;"><img src="./assets/repo_wisebiz-gitops.svg?v=15" alt="K8s GitOps Resource" style="display: block;"></a>
  <a href="https://github.com/Adithya-Meda/wisebiz-terraform" style="display: block;"><img src="./assets/repo_wisebiz-terraform.svg?v=15" alt="Wisebiz Terraform Resource" style="display: block;"></a>
</div>
</div>
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

# Cleanup old fragments
for file in os.listdir("assets"):
    if file.startswith("blueprint_") and file != "blueprint_main.svg":
        os.remove(os.path.join("assets", file))

