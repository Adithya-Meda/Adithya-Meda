with open("build.py", "r", encoding="utf-8") as f:
    build = f.read()

# Completely rename the file to something GitHub has never seen before
build = build.replace('blueprint_final.svg', 'blueprint_v100.svg')

with open("build.py", "w", encoding="utf-8") as f:
    f.write(build)

import os
os.system("python build.py")
