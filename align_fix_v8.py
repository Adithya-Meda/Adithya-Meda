with open("build.py", "r", encoding="utf-8") as f:
    build = f.read()

# 1. Restore the background logic by putting defs_premium() back inside the repo generation
build = build.replace('svg = f\'\'\'<svg width="{width}" height="140" xmlns="http://www.w3.org/2000/svg">\n  {defs_only()}', 'svg = f\'\'\'<svg width="{width}" height="140" xmlns="http://www.w3.org/2000/svg">\n  {defs_premium()}')

# 2. Revert the width of the cards from 395 back to 400
build = build.replace('width = 800 if is_centered_wide else 395', 'width = 800 if is_centered_wide else 400')
# Revert the internal rect width from {width-5} back to {width-10}
build = build.replace('width="{width-5}"', 'width="{width-10}"')

# 3. Add line-height: 0 to the wrapper div to remove vertical gaps
build = build.replace('readme = f\'\'\'<div align="center">', 'readme = f\'\'\'<div align="center" style="line-height: 0; font-size: 0;">')

with open("build.py", "w", encoding="utf-8") as f:
    f.write(build)

import os
os.system("python build.py")

import time
v = int(time.time())
print(f"Updated cache buster to {v}")
