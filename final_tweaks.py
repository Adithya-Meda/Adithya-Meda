with open("build.py", "r", encoding="utf-8") as f:
    build = f.read()

# 1. Fix "India ----------"
build = build.replace('region_text = f"REGION: {p.get(\'region\', \'GLOBAL\')}"', 'region_text = f"REGION: {p.get(\'region\', \'GLOBAL\')} ----------"')
build = build.replace('cutout_width = len(region_text) * 8 + 40', 'cutout_width = len(region_text) * 8 + 20')

# 2. Fix philosophy text clipping (move the whole text group UP by 15px)
build = build.replace('transform="translate(40, 61)"', 'transform="translate(40, 46)"')

# 3. Fix repo cards wrapping by slightly reducing their width from 400 to 395
build = build.replace('width = 800 if is_centered_wide else 400', 'width = 800 if is_centered_wide else 395')
# And adjust the internal rect width to match
build = build.replace('width="{width-10}"', 'width="{width-5}"')

with open("build.py", "w", encoding="utf-8") as f:
    f.write(build)

import os
os.system("python build.py")

# Ensure the README uses the new version tag
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

readme = readme.replace("?v=17", "?v=18")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
