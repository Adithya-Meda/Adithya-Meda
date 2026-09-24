with open("build.py", "r", encoding="utf-8") as f:
    build = f.read()

# Add defs_only function right after defs_premium
defs_only_func = """
def defs_only():
    return defs_premium().split("<rect width=")[0]
"""

build = build.replace('def defs_premium():', defs_only_func + '\ndef defs_premium():')

# Replace defs_premium with defs_only in the repo generation
build = build.replace(
    'svg = f\'\'\'<svg width="{width}" height="140" xmlns="http://www.w3.org/2000/svg">\n  {defs_premium()}',
    'svg = f\'\'\'<svg width="{width}" height="140" xmlns="http://www.w3.org/2000/svg">\n  {defs_only()}'
)

with open("build.py", "w", encoding="utf-8") as f:
    f.write(build)

import os
os.system("python build.py")

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

readme = readme.replace("?v=3", "?v=4")
readme = readme.replace("?v=2", "?v=4")
readme = readme.replace("?v=1", "?v=4")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
