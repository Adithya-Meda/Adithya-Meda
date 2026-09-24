import os
import html
import json
import urllib.request

os.makedirs("assets", exist_ok=True)

# ==========================================
# 🔧 USER CONFIGURATION - EDIT YOUR DETAILS HERE!
# ==========================================
CONFIG = {
    "theme": {
        "BG_COLOR": "#0a192f",
        "GRID_COLOR": "#172a45",
        "LINE_COLOR": "#64ffda",
        "TEXT_MAIN": "#e6f1ff",
        "TEXT_DIM": "#8892b0",
        "NODE_BG": "#112240"
    },
    "profile": {
        "github_username": "Adithya-Meda",
        "region": "India",
        "title": "Senior DevOps Engineer",
        "subtitle": "< Automating Infrastructure at Scale />"
    },
    "philosophy": {
        "automation": "Everything as Code",
        "security": "Shift-Left & Zero Trust"
    },
    "dns_records": [
        {"name": "linkedin", "type": "CNAME", "value": "linkedin.com/in/adithya-m-s-95411b83/", "color": "#64ffda"},
        {"name": "email", "type": "MX", "value": "mailto:adithyams93@outlook.com", "color": "#BC8CFF"},
        {"name": "medium", "type": "A", "value": "medium.com/@adithyameda", "color": "#FF9900"},
        {"name": "hashnode", "type": "A", "value": "hashnode.com/@adithyameda", "color": "#FF9900"},
        {"name": "Digital Badges", "type": "A", "value": "credly.com/users/adithya-ms.f90708a6/badges/credly", "color": "#FF9900"}
    ],
    "skills": [
        ("AWS", 150),
        ("Kubernetes", 270),
        ("Terraform", 390),
        ("Docker", 510),
        ("CI/CD", 630)
    ],
    "stats": {
        "commits": 1450,
        "prs": 120,
        "issues": 45,
        "uptime": "99%"
    },
    "repos": [
        {"name": "wisebiz-ecommerce-app", "desc": "Microservices based E-commerce platform"},
        {"name": "wisebiz-gitops", "desc": "Automated deployment with ArgoCD"},
        {"name": "wisebiz-terraform", "desc": "Terraform modules for Cloud Infrastructure"}
    ]
}
# ==========================================

# Apply theme globally for easy access
T = CONFIG["theme"]

def write_svg(filename, content):
    with open(f"assets/{filename}", "w", encoding="utf-8") as f:
        f.write(content)

def defs_premium():
    return f"""
  <defs>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{T['GRID_COLOR']}" stroke-width="1"/>
      <circle cx="40" cy="40" r="1" fill="{T['GRID_COLOR']}" />
    </pattern>
    <filter id="drop-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#020c1b" flood-opacity="0.8"/>
    </filter>
    <filter id="neon-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="blur1" />
      <feGaussianBlur in="SourceGraphic" stdDeviation="8" result="blur2" />
      <feMerge>
        <feMergeNode in="blur2" />
        <feMergeNode in="blur1" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <linearGradient id="chart-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{T['LINE_COLOR']}" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="{T['LINE_COLOR']}" stop-opacity="0.0"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="{T['BG_COLOR']}" />
  <rect width="100%" height="100%" fill="url(#grid)" />
"""

def generate_blueprint_header():
    p = CONFIG["profile"]
    
    # Dynamically calculate the cutout width so the dashed border hugs the text
    region_text = f"REGION: {p['region']}"
    cutout_width = int(len(region_text) * 7.0 + 0)
    
    svg = f"""<svg width="800" height="280" xmlns="http://www.w3.org/2000/svg">
  {defs_premium()}
  
  <rect x="20" y="20" width="760" height="240" fill="none" stroke="{T['TEXT_DIM']}" stroke-width="1" stroke-dasharray="10,5" rx="12"/>
  <rect x="40" y="10" width="{cutout_width}" height="20" fill="{T['BG_COLOR']}"/>
  <text x="50" y="25" font-family="sans-serif" font-size="12" fill="{T['TEXT_DIM']}" font-weight="bold">{region_text}</text>

  <path id="data-path" d="M 180 90 C 220 90, 220 150, 270 150" fill="none" stroke="{T['LINE_COLOR']}" stroke-width="2" stroke-dasharray="4,4"/>
  <circle r="4" fill="#fff" filter="url(#neon-glow)">
    <animateMotion dur="2s" repeatCount="indefinite"><mpath href="#data-path"/></animateMotion>
  </circle>

  <g transform="translate(40, 60)" filter="url(#drop-shadow)">
    <rect width="140" height="60" fill="{T['NODE_BG']}" stroke="{T['LINE_COLOR']}" stroke-width="1" rx="8"/>
    <circle cx="20" cy="30" r="6" fill="none" stroke="{T['LINE_COLOR']}" stroke-width="2"/>
    <circle cx="20" cy="30" r="2" fill="{T['LINE_COLOR']}"/>
    <text x="40" y="27" font-family="sans-serif" font-size="10" fill="{T['TEXT_DIM']}">INGRESS ROUTER</text>
    <text x="40" y="45" font-family="monospace" font-size="14" fill="{T['TEXT_MAIN']}" font-weight="bold">App ALB</text>
  </g>

  <g transform="translate(270, 80)" filter="url(#drop-shadow)">
    <rect width="320" height="140" fill="{T['NODE_BG']}" stroke="{T['LINE_COLOR']}" stroke-width="2" rx="12" />
    <circle cx="15" cy="15" r="4" fill="#FF5F56"/>
    <circle cx="30" cy="15" r="4" fill="#FFBD2E"/>
    <circle cx="45" cy="15" r="4" fill="#27C93F"/>
    <text x="160" y="45" font-family="sans-serif" font-size="24" fill="{T['TEXT_MAIN']}" font-weight="bold" text-anchor="middle">{html.escape(p["title"])}</text>
    <text x="160" y="70" font-family="monospace" font-size="12" fill="{T['LINE_COLOR']}" text-anchor="middle">{html.escape(p["subtitle"])}</text>
    
    <circle cx="160" cy="105" r="14" fill="none" stroke="{T['GRID_COLOR']}" stroke-width="3"/>
    <circle cx="160" cy="105" r="14" fill="none" stroke="{T['LINE_COLOR']}" stroke-width="3" stroke-dasharray="80" stroke-dashoffset="0">
      <animate attributeName="stroke-dashoffset" values="80;0;80" dur="4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="160" cy="105" r="6" fill="{T['LINE_COLOR']}" filter="url(#neon-glow)"/>
  </g>

  <path id="db-path" d="M 590 150 C 640 150, 640 110, 670 110" fill="none" stroke="{T['LINE_COLOR']}" stroke-width="2" stroke-dasharray="4,4"/>
  <circle r="4" fill="#fff" filter="url(#neon-glow)">
    <animateMotion dur="2.5s" repeatCount="indefinite" keyPoints="1;0" keyTimes="0;1" calcMode="linear"><mpath href="#db-path"/></animateMotion>
  </circle>

  <g transform="translate(670, 80)" filter="url(#drop-shadow)">
    <path d="M 0 15 Q 40 -5 80 15 L 80 55 Q 40 75 0 55 Z" fill="{T['NODE_BG']}" stroke="{T['LINE_COLOR']}" stroke-width="2"/>
    <path d="M 0 15 Q 40 35 80 15" fill="none" stroke="{T['LINE_COLOR']}" stroke-width="2"/>
    <text x="40" y="45" font-family="monospace" font-size="12" fill="{T['TEXT_MAIN']}" font-weight="bold" text-anchor="middle">Brain.db</text>
  </g>
</svg>"""
    write_svg("blueprint_header.svg", svg)

def generate_dns_socials():
    records = CONFIG["dns_records"]
    
    # 1. Header
    svg_header = f'''<svg width="800" height="80" xmlns="http://www.w3.org/2000/svg">
  {defs_premium()}
  <text x="40" y="35" font-family="sans-serif" font-size="14" fill="{T['TEXT_DIM']}" font-weight="bold" letter-spacing="1">ROUTE53 DNS RECORDS (CONTACTS &amp; CERTS)</text>
  <line x1="20" y1="50" x2="780" y2="50" stroke="{T['GRID_COLOR']}" stroke-width="2"/>
  <text x="40" y="70" font-family="monospace" font-size="12" fill="{T['TEXT_DIM']}" font-weight="bold">RECORD NAME</text>
  <text x="230" y="70" font-family="monospace" font-size="12" fill="{T['TEXT_DIM']}" font-weight="bold">TYPE</text>
  <text x="310" y="70" font-family="monospace" font-size="12" fill="{T['TEXT_DIM']}" font-weight="bold">ROUTING VALUE</text>
  <text x="700" y="70" font-family="monospace" font-size="12" fill="{T['TEXT_DIM']}" font-weight="bold">STATUS</text>
</svg>'''
    write_svg("blueprint_dns_header.svg", svg_header)

    # 2. Rows
    for i, r in enumerate(records):
        svg_row = f'''<svg width="800" height="40" xmlns="http://www.w3.org/2000/svg">
  {defs_premium()}
  <rect x="20" y="0" width="760" height="35" fill="{T['NODE_BG']}" fill-opacity="0.6" stroke="{T['TEXT_DIM']}" stroke-opacity="0.4" stroke-width="1" rx="6" />
  <text x="40" y="22" font-family="sans-serif" font-size="14" fill="{T['TEXT_MAIN']}">{r['name']}</text>
  <rect x="230" y="9" width="60" height="18" fill="{r['color']}" fill-opacity="0.2" rx="4"/>
  <text x="260" y="22" font-family="monospace" font-size="12" fill="{r['color']}" text-anchor="middle">{r['type']}</text>
  <text x="310" y="22" font-family="monospace" font-size="12" fill="{T['TEXT_MAIN']}">{r['value']}</text>
  <circle cx="700" cy="17" r="4" fill="#27C93F"/><text x="715" y="22" font-family="sans-serif" font-size="12" fill="{T['TEXT_DIM']}">Active</text>
  <style>rect:hover {{ stroke: {T['LINE_COLOR']}; }}</style>
</svg>'''
        write_svg(f"blueprint_dns_row_{i}.svg", svg_row)

def generate_philosophy():
    p = CONFIG["philosophy"]
    svg = f"""<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  {defs_premium()}
  
  <rect x="20" y="10" width="760" height="170" fill="{T['NODE_BG']}" stroke="{T['LINE_COLOR']}" stroke-width="1" rx="8" filter="url(#drop-shadow)"/>
  <rect x="20" y="10" width="760" height="25" fill="{T['GRID_COLOR']}" rx="8"/>
  <text x="40" y="27" font-family="sans-serif" font-size="12" fill="{T['TEXT_DIM']}" font-weight="bold" letter-spacing="1">CONFIGMAP: ENGINEERING_PHILOSOPHY.YAML</text>
  
  <g font-family="monospace" font-size="14" fill="{T['TEXT_MAIN']}" transform="translate(40, 60)">
    <text y="0"><tspan fill="#FFBD2E">apiVersion:</tspan> v1</text>
    <text y="20"><tspan fill="#FFBD2E">kind:</tspan> CoreValues</text>
    <text y="40"><tspan fill="#FFBD2E">data:</tspan></text>
    <text y="60">  <tspan fill="{T['LINE_COLOR']}">automation:</tspan> "{html.escape(p.get("automation", ""))}"</text>
    <text y="80">  <tspan fill="{T['LINE_COLOR']}">security:</tspan> "{html.escape(p.get("security", ""))}"</text>"""
    
    if "learning" in p and p["learning"]:
        mastering_str = '", "'.join(p['learning'])
        svg += f"""\n    <text y="100">  <tspan fill="{T['LINE_COLOR']}">currently_mastering:</tspan> ["{mastering_str}"]</text>"""

    svg += """\n  </g>\n</svg>"""
    write_svg("blueprint_philosophy.svg", svg)

def generate_skills_diagram():
    svg = f"""<svg width="800" height="180" xmlns="http://www.w3.org/2000/svg">\n  {defs_premium()}\n  <text x="400" y="25" font-family="sans-serif" font-size="12" fill="{T['TEXT_DIM']}" font-weight="bold" letter-spacing="2" text-anchor="middle">TECH STACK TOPOLOGY (SUBNETS)</text>\n  <line x1="100" y1="130" x2="700" y2="130" stroke="{T['TEXT_DIM']}" stroke-width="2" stroke-dasharray="5,5"/>\n  """
    for i, (name, x) in enumerate(CONFIG["skills"]):
        y_offset = 60 if i % 2 == 0 else 90
        svg += f"""
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
  </g>"""
    svg += "\n</svg>"
    write_svg("blueprint_skills.svg", svg)
def fetch_github_stats(username):
    headers = {'User-Agent': 'Mozilla/5.0'}
    stats = {"commits": 0, "prs": 0, "issues": 0}
    try:
        # Commits (Requires special Accept header)
        req = urllib.request.Request(f"https://api.github.com/search/commits?q=author:{username}", headers={**headers, 'Accept': 'application/vnd.github.cloak-preview'})
        with urllib.request.urlopen(req) as response:
            stats["commits"] = json.loads(response.read().decode()).get("total_count", 0)
            
        # PRs
        req = urllib.request.Request(f"https://api.github.com/search/issues?q=author:{username}+type:pr", headers=headers)
        with urllib.request.urlopen(req) as response:
            stats["prs"] = json.loads(response.read().decode()).get("total_count", 0)
            
        # Issues
        req = urllib.request.Request(f"https://api.github.com/search/issues?q=author:{username}+type:issue", headers=headers)
        with urllib.request.urlopen(req) as response:
            stats["issues"] = json.loads(response.read().decode()).get("total_count", 0)
            
        return stats
    except Exception as e:
        print(f"Failed to fetch real stats: {e}")
        return None

def generate_stats_github():
    stats = CONFIG["stats"]
    username = CONFIG["profile"].get("github_username", "")
    
    label1 = "Total Commits"
    val1 = stats['commits']
    label2 = "Total PRs"
    val2 = stats['prs']
    label3 = "Total Issues"
    val3 = stats['issues']
    
    if username:
        real = fetch_github_stats(username)
        if real:
            val1 = real['commits']
            val2 = real['prs']
            val3 = real['issues']

    svg = f"""<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  {defs_premium()}
  <rect x="20" y="10" width="760" height="170" fill="{T['NODE_BG']}" stroke="{T['GRID_COLOR']}" stroke-width="2" rx="12" filter="url(#drop-shadow)"/>
  <text x="40" y="35" font-family="sans-serif" font-size="14" fill="{T['TEXT_DIM']}" font-weight="bold" letter-spacing="1">GITHUB STATS</text>
  <g transform="translate(40, 60)">
    <text x="0" y="10" font-family="sans-serif" font-size="12" fill="{T['TEXT_DIM']}">{label1}</text>
    <text x="0" y="45" font-family="monospace" font-size="32" fill="{T['TEXT_MAIN']}" font-weight="bold">{val1}</text>
    <path d="M 120 40 C 135 40, 140 20, 155 20 C 170 20, 175 10, 190 10 C 205 10, 210 30, 225 30 L 225 50 L 120 50 Z" fill="url(#chart-grad)"/>
    <path d="M 120 40 C 135 40, 140 20, 155 20 C 170 20, 175 10, 190 10 C 205 10, 210 30, 225 30" fill="none" stroke="{T['LINE_COLOR']}" stroke-width="2"/>
  </g>
  <g transform="translate(290, 60)">
    <text x="0" y="10" font-family="sans-serif" font-size="12" fill="{T['TEXT_DIM']}">{label2}</text>
    <text x="0" y="45" font-family="monospace" font-size="32" fill="{T['TEXT_MAIN']}" font-weight="bold">{val2}</text>
    <path d="M 140 30 C 155 30, 160 40, 175 40 C 190 40, 195 10, 210 10 C 225 10, 230 20, 245 20 L 245 50 L 140 50 Z" fill="url(#chart-grad)"/>
    <path d="M 140 30 C 155 30, 160 40, 175 40 C 190 40, 195 10, 210 10 C 225 10, 230 20, 245 20" fill="none" stroke="{T['LINE_COLOR']}" stroke-width="2"/>
  </g>
  <g transform="translate(620, 95)">
    <circle cx="0" cy="0" r="30" fill="none" stroke="{T['GRID_COLOR']}" stroke-width="6"/>
    <circle cx="0" cy="0" r="30" fill="none" stroke="{T['LINE_COLOR']}" stroke-width="6" stroke-dasharray="188" stroke-dashoffset="40" stroke-linecap="round">
      <animate attributeName="stroke-dashoffset" from="188" to="40" dur="2s" fill="freeze"/>
    </circle>
    <text x="0" y="5" font-family="monospace" font-size="20" fill="{T['TEXT_MAIN']}" font-weight="bold" text-anchor="middle">{val3}</text>
    <text x="0" y="50" font-family="sans-serif" font-size="12" fill="{T['TEXT_DIM']}" text-anchor="middle">{label3}</text>
  </g>
</svg>"""
    write_svg("blueprint_stats.svg", svg)

def generate_repo_blueprint(name, desc, is_centered_wide=False):
    filename = name.replace(" ", "_").lower()
    
    width = 800 if is_centered_wide else 400
    offset_x = 200 if is_centered_wide else 0
    
    svg = f"""<svg width="{width}" height="140" xmlns="http://www.w3.org/2000/svg">
  {defs_premium()}
  <rect x="{15 + offset_x}" y="10" width="370" height="120" fill="{T['NODE_BG']}" fill-opacity="0.9" stroke="{T['GRID_COLOR']}" stroke-width="2" rx="10" filter="url(#drop-shadow)"/>
  <circle cx="{45 + offset_x}" cy="40" r="16" fill="none" stroke="{T['LINE_COLOR']}" stroke-width="2"/>
  <circle cx="{45 + offset_x}" cy="40" r="6" fill="{T['LINE_COLOR']}" filter="url(#neon-glow)"/>
  <text x="{75 + offset_x}" y="45" font-family="monospace" font-size="18" fill="{T['TEXT_MAIN']}" font-weight="bold">{name}</text>
  <text x="{35 + offset_x}" y="80" font-family="sans-serif" font-size="13" fill="{T['TEXT_DIM']}">{desc}</text>
  <rect x="{35 + offset_x}" y="100" width="10" height="10" fill="{T['LINE_COLOR']}" rx="2"/>
  <text x="{55 + offset_x}" y="110" font-family="monospace" font-size="11" fill="{T['LINE_COLOR']}" letter-spacing="1">ACTIVE DEPLOYMENT</text>
  <style>rect:hover {{ stroke: {T['LINE_COLOR']}; }}</style>
</svg>"""
    write_svg(f"repo_{filename}.svg", svg)

if __name__ == "__main__":
    generate_blueprint_header()
    generate_philosophy()
    generate_dns_socials()
    generate_skills_diagram()
    generate_stats_github()
    
    repos = CONFIG["repos"]
    for i, repo in enumerate(repos):
        is_last = (i == len(repos) - 1)
        is_odd_total = (len(repos) % 2 != 0)
        is_centered_wide = (is_last and is_odd_total)
        generate_repo_blueprint(repo['name'], repo['desc'], is_centered_wide)
        
    print("Added deep profile info SVGs!")

