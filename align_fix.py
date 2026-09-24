with open("build.py", "r", encoding="utf-8") as f:
    build = f.read()

build = build.replace('cutout_width = 115', 'cutout_width = 100')

with open("build.py", "w", encoding="utf-8") as f:
    f.write(build)

import os
os.system("python build.py")

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()
readme = readme.replace("?v=19", "?v=20")
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
