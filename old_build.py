import os
import json
import urllib.request
from datetime import datetime

CONFIG = {
    "name": "Adithya M S",
    "role": "Senior DevOps Engineer",
    "subtitle": "< Automating Infrastructure at Scale />",
    "region": "India",
    "philosophy": {
        "automation": "Everything as Code",
        "security": "Shift-Left & Zero Trust"
    },
    "dns_records": [
        {"name": "linkedin", "type": "CNAME", "value": "linkedin.com/in/adithya-m-s-95411b83/", "color": "#0077B5"},
        {"name": "email", "type": "MX", "value": "mailto:adithyams93@outlook.com", "color": "#6444B6"},
        {"name": "medium", "type": "A", "value": "medium.com/@adithyameda", "color": "#6444B6"},
        {"name": "hashnode", "type": "A", "value": "hashnode.com/@adithyameda", "color": "#6444B6"},
        {"name": "Digital Badges", "type": "A", "value": "credly.com/users/adithya-ms.f90708a6/badges/credly", "color": "#6444B6"}
    ],
    "skills": [
        ("AWS", 150),
        ("Terraform", 310),
        ("CI/CD", 470),
        ("Docker", 630),
        ("Kubernetes", 780)
    ]
}

T = {
    "BG_COLOR": "#0a192f",
    "GRID_COLOR": "#172a45",
    "TEXT_MAIN": "#ccd6f6",
    "TEXT_DIM": "#8892b0",
    "LINE_COLOR": "#64ffda",
    "NODE_BG": "#112240"
}

def defs_premium():
    return f'''
  <defs>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{T['GRID_COLOR']}" stroke-width="0.5"/>
    </pattern>
    <linearGradient id="glow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{T['LINE_COLOR']}" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#0284c7" stop-opacity="0.8" />
    </linearGradient>
    <filter id="drop-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>
  <rect width="100%" height="100%" fill="{T['BG_COLOR']}" />
  <rect width="100%" height="100%" fill="url(#grid)" />
'''

def write_svg(filename, content):
    os.makedirs("assets", exist_ok=True)
    with open(f"assets/{filename}", "w", encoding="utf-8") as f:
        f.write(content)

def generate_blueprint_top():
    region_text = f"REGION: {CONFIG['region']}"
    # Header block is 0 to 280.
    # Philosophy block is 280 to 460.
    # DNS header is 460 to 540.
    # Total height = 540
    
    svg = f'''<svg width="800" height="540" xmlns="http://www.w3.org/2000/svg">
  {defs_premium()}
  
  <!-- HEADER BLOCK (0-280) -->
  <rect x="20" y="20" width="760" height="240" fill="none" stroke="{T['TEXT_DIM']}" stroke-width="1" stroke-dasharray="10,5" rx="12"/>
  <rect x="40" y="10" width="140" height="20" fill="{T['BG_COLOR']}"/>
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
      <text x="160" y="55" font-family="sans-serif" font-size="28" fill="{T['TEXT_MAIN']}" font-weight="bold" text-anchor="middle">{CONFIG['name']}</text>
      <text x="160" y="85" font-family="monospace" font-size="14" fill="{T['LINE_COLOR']}" font-weight="bold" text-anchor="middle">{CONFIG['subtitle']}</text>
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

  <!-- PHILOSOPHY BLOCK (280-460) -->
  <g transform="translate(0, 280)">
    <rect x="20" y="20" width="760" height="140" fill="{T['NODE_BG']}" fill-opacity="0.8" stroke="{T['LINE_COLOR']}" stroke-width="1" rx="8"/>
    <text x="40" y="45" font-family="sans-serif" font-size="12" fill="{T['TEXT_DIM']}" font-weight="bold" letter-spacing="1">CONFIGMAP: ENGINEERING_PHILOSOPHY.YAML</text>
    <g font-family="monospace" font-size="14" fill="{T['TEXT_MAIN']}" transform="translate(40, 80)">
      <text x="0" y="0"><tspan fill="#FFBD2E">apiVersion:</tspan> v1</text>
      <text x="0" y="25"><tspan fill="#FFBD2E">kind:</tspan> CoreValues</text>
      <text x="0" y="50"><tspan fill="#FFBD2E">data:</tspan></text>
      <text x="0" y="75"><tspan fill="{T['LINE_COLOR']}">automation:</tspan> "{CONFIG['philosophy']['automation']}"</text>
      <text x="0" y="100"><tspan fill="{T['LINE_COLOR']}">security:</tspan> "{CONFIG['philosophy']['security']}"</text>
    </g>
  </g>

  <!-- DNS HEADER BLOCK (460-540) -->
  <g transform="translate(0, 460)">
    <text x="40" y="35" font-family="sans-serif" font-size="14" fill="{T['TEXT_DIM']}" font-weight="bold" letter-spacing="1">ROUTE53 DNS RECORDS (CONTACTS &amp; CERTS)</text>
    <line x1="20" y1="50" x2="780" y2="50" stroke="{T['GRID_COLOR']}" stroke-width="2"/>
    <text x="40" y="70" font-family="monospace" font-size="12" fill="{T['TEXT_DIM']}" font-weight="bold">RECORD NAME</text>
    <text x="230" y="70" font-family="monospace" font-size="12" fill="{T['TEXT_DIM']}" font-weight="bold">TYPE</text>
    <text x="310" y="70" font-family="monospace" font-size="12" fill="{T['TEXT_DIM']}" font-weight="bold">ROUTING VALUE</text>
    <text x="700" y="70" font-family="monospace" font-size="12" fill="{T['TEXT_DIM']}" font-weight="bold">STATUS</text>
  </g>

</svg>'''
    write_svg("blueprint_top.svg", svg)

def generate_blueprint_bottom():
    # Tech Stack (0-180)
    # Stats (180-320) -> Let's give stats 140px. Total = 320
    # Add stats fetching
    try:
        req = urllib.request.Request("https://api.github.com/search/commits?q=author:Adithya-Meda", headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req)
        commits = json.loads(res.read())['total_count']
    except: commits = 1337
    try:
        req = urllib.request.Request("https://api.github.com/search/issues?q=author:Adithya-Meda+type:pr", headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req)
        prs = json.loads(res.read())['total_count']
    except: prs = 42
    try:
        req = urllib.request.Request("https://api.github.com/search/issues?q=author:Adithya-Meda+type:issue", headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req)
        issues = json.loads(res.read())['total_count']
    except: issues = 11

    svg = f'''<svg width="800" height="320" xmlns="http://www.w3.org/2000/svg">
  {defs_premium()}
  
  <!-- TECH STACK (0-180) -->
  <g transform="translate(0, 0)">
    <text x="400" y="25" font-family="sans-serif" font-size="12" fill="{T['TEXT_DIM']}" font-weight="bold" letter-spacing="2" text-anchor="middle">TECH STACK TOPOLOGY (SUBNETS)</text>
    <line x1="100" y1="130" x2="700" y2="130" stroke="{T['TEXT_DIM']}" stroke-width="2" stroke-dasharray="5,5"/>
'''
    for i, (name, x) in enumerate(CONFIG["skills"]):
        y_offset = 60 if i % 2 == 0 else 90
        svg += f'''
    <path d="M {x} {y_offset+15} C {x} {y_offset+30}, {x} 130, {x} 130" fill="none" stroke="{T['LINE_COLOR']}" stroke-width="2"/>
    <circle cx="{x}" cy="130" r="4" fill="{T['LINE_COLOR']}">
      <animate attributeName="opacity" values="1;0.2;1" dur="{1.5 + i*0.3}s" repeatCount="indefinite"/>
    </circle>
    <g transform="translate({x-50}, {y_offset-15})" filter="url(#drop-shadow)">
      <rect width="100" height="30" fill="{T['NODE_BG']}" stroke="{T['LINE_COLOR']}" stroke-width="1" rx="15"/>
      <text x="50" y="20" font-family="monospace" font-size="12" fill="{T['TEXT_MAIN']}" font-weight="bold" text-anchor="middle">{name}</text>
    </g>'''
    
    svg += f'''
  </g>
  
  <!-- STATS BLOCK (180-320) -->
  <g transform="translate(0, 180)">
    <text x="40" y="35" font-family="sans-serif" font-size="14" fill="{T['TEXT_DIM']}" font-weight="bold" letter-spacing="1">GITHUB STATS</text>
    <g transform="translate(40, 60)">
      <!-- Box 1 -->
      <g transform="translate(0, 0)">
        <rect width="220" height="60" fill="{T['NODE_BG']}" stroke="{T['GRID_COLOR']}" stroke-width="1" rx="6"/>
        <text x="20" y="35" font-family="sans-serif" font-size="12" fill="{T['TEXT_DIM']}">Total Commits</text>
        <text x="200" y="37" font-family="monospace" font-size="20" fill="{T['LINE_COLOR']}" font-weight="bold" text-anchor="end">{commits}</text>
      </g>
      <!-- Box 2 -->
      <g transform="translate(250, 0)">
        <rect width="220" height="60" fill="{T['NODE_BG']}" stroke="{T['GRID_COLOR']}" stroke-width="1" rx="6"/>
        <text x="20" y="35" font-family="sans-serif" font-size="12" fill="{T['TEXT_DIM']}">Pull Requests</text>
        <text x="200" y="37" font-family="monospace" font-size="20" fill="{T['LINE_COLOR']}" font-weight="bold" text-anchor="end">{prs}</text>
      </g>
      <!-- Box 3 -->
      <g transform="translate(500, 0)">
        <rect width="220" height="60" fill="{T['NODE_BG']}" stroke="{T['GRID_COLOR']}" stroke-width="1" rx="6"/>
        <text x="20" y="35" font-family="sans-serif" font-size="12" fill="{T['TEXT_DIM']}">Issues Logged</text>
        <text x="200" y="37" font-family="monospace" font-size="20" fill="{T['LINE_COLOR']}" font-weight="bold" text-anchor="end">{issues}</text>
      </g>
    </g>
  </g>

</svg>'''
    write_svg("blueprint_bottom.svg", svg)

def generate_dns_rows():
    for i, r in enumerate(CONFIG["dns_records"]):
        svg = f'''<svg width="800" height="36" xmlns="http://www.w3.org/2000/svg">
  {defs_premium()}
  <rect x="20" y="1" width="760" height="34" fill="{T['NODE_BG']}" stroke="{T['LINE_COLOR']}" stroke-width="1" rx="4" />
  <text x="40" y="23" font-family="sans-serif" font-size="14" fill="{T['TEXT_MAIN']}">{r['name']}</text>
  <rect x="230" y="10" width="60" height="18" fill="{r['color']}" fill-opacity="0.2" rx="4"/>
  <text x="260" y="23" font-family="sans-serif" font-size="10" fill="{r['color']}" text-anchor="middle" font-weight="bold">{r['type']}</text>
  <text x="310" y="23" font-family="monospace" font-size="12" fill="{T['TEXT_DIM']}">{r['value']}</text>
  <circle cx="700" cy="18" r="4" fill="#27C93F"/><text x="715" y="23" font-family="sans-serif" font-size="12" fill="{T['TEXT_DIM']}">Active</text>
  <style>rect:hover {{ stroke: #ffffff; stroke-width: 2px; }}</style>
</svg>'''
        write_svg(f"blueprint_dns_{i}.svg", svg)

def generate_repo_card(repo_name, desc):
    try:
        req = urllib.request.Request(f"https://api.github.com/repos/Adithya-Meda/{repo_name}", headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req)
        data = json.loads(res.read())
        stars = data.get("stargazers_count", 0)
        forks = data.get("forks_count", 0)
        lang = data.get("language", "HCL")
    except:
        stars, forks, lang = 0, 0, "Unknown"
        
    width = 240
    svg = f'''<svg width="{width}" height="140" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="shadow">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#000000" flood-opacity="0.3"/>
    </filter>
  </defs>
  <rect width="100%" height="100%" fill="{T['BG_COLOR']}" />
  <rect width="{width-10}" height="130" x="5" y="5" fill="{T['NODE_BG']}" stroke="{T['GRID_COLOR']}" stroke-width="1" rx="8" filter="url(#shadow)"/>
  <text x="20" y="30" font-family="sans-serif" font-size="14" fill="{T['LINE_COLOR']}" font-weight="bold">📦 {repo_name}</text>
  <text x="20" y="55" font-family="sans-serif" font-size="11" fill="{T['TEXT_DIM']}">{desc}</text>
  
  <g transform="translate(20, 100)" font-family="monospace" font-size="12" fill="{T['TEXT_DIM']}">
    <circle cx="5" cy="-4" r="4" fill="#FFBD2E"/>
    <text x="15" y="0">{lang}</text>
    <text x="80" y="0">⭐ {stars}</text>
    <text x="130" y="0">🍴 {forks}</text>
  </g>
  <style>rect:hover {{ stroke: {T['LINE_COLOR']}; stroke-width: 2px; cursor: pointer; }}</style>
</svg>'''
    write_svg(f"repo_{repo_name}.svg", svg)

if __name__ == "__main__":
    generate_blueprint_top()
    generate_dns_rows()
    generate_blueprint_bottom()
    generate_repo_card("wisebiz-ecommerce-app", "Microservices application codebase")
    generate_repo_card("wisebiz-gitops", "ArgoCD and Kubernetes manifests")
    generate_repo_card("wisebiz-terraform", "AWS Infrastructure as Code")
    print("Generated unified SVGs!")
