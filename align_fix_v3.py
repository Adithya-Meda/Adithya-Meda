with open("build.py", "r", encoding="utf-8") as f:
    build = f.read()

# Fix the translation to move text up by 20px
build = build.replace('transform="translate(40, 80)"', 'transform="translate(40, 60)"')

with open("build.py", "w", encoding="utf-8") as f:
    f.write(build)

import os
os.system("python build.py")

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()
readme = readme.replace("?v=1", "?v=2")
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
