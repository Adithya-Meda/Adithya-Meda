with open("build.py", "r", encoding="utf-8") as f:
    build = f.read()

# 1. Ensure defs_only exists and is used in generate_repo_blueprint
defs_only_code = """
def defs_only():
    return defs_premium().split("<rect width=")[0]
"""
if "def defs_only():" not in build:
    build = build.replace('def defs_premium():', defs_only_code + '\ndef defs_premium():')

# Make repo cards completely transparent by removing the background grid
build = build.replace('{defs_premium()}', '{defs_only()}')
# Put defs_premium back ONLY for the main blueprint graphic
build = build.replace('svg = f\'\'\'<svg width="800" height="840" xmlns="http://www.w3.org/2000/svg">\n  {defs_only()}', 'svg = f\'\'\'<svg width="800" height="840" xmlns="http://www.w3.org/2000/svg">\n  {defs_premium()}')

# 2. Rename the repo output files to definitively bypass GitHub's image cache
build = build.replace('write_svg(f"repo_{filename}.svg", svg)', 'write_svg(f"repo_v101_{filename}.svg", svg)')

# 3. Update the README generation logic to point to the new uncached filenames
build = build.replace('repo_wisebiz-ecommerce-app.svg', 'repo_v101_wisebiz-ecommerce-app.svg')
build = build.replace('repo_wisebiz-gitops.svg', 'repo_v101_wisebiz-gitops.svg')
build = build.replace('repo_wisebiz-terraform.svg', 'repo_v101_wisebiz-terraform.svg')

with open("build.py", "w", encoding="utf-8") as f:
    f.write(build)

import os
os.system("python build.py")

import time
print(f"Busted cache!")
