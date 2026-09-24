with open("build.py", "r", encoding="utf-8") as f:
    build = f.read()

build = build.replace('region_text = f"REGION: {p.get(\'region\', \'GLOBAL\')} ----------"', 'region_text = f"REGION: {p.get(\'region\', \'GLOBAL\')}"')
build = build.replace('cutout_width = len(region_text) * 8 + 20', 'cutout_width = 115')

with open("build.py", "w", encoding="utf-8") as f:
    f.write(build)

import os
os.system("python build.py")

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()
readme = readme.replace("?v=18", "?v=19")
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
