with open("build.py", "r", encoding="utf-8") as f:
    build = f.read()

# Reduce cutout_width to 85 to reveal one more dash
build = build.replace('cutout_width = 100', 'cutout_width = 85')

# Rename the output file to completely bypass GitHub CDN cache
build = build.replace('write_svg("blueprint_main.svg", svg)', 'write_svg("blueprint_final.svg", svg)')

with open("build.py", "w", encoding="utf-8") as f:
    f.write(build)

import os
os.system("python build.py")

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Update README to use the new filename
readme = readme.replace("blueprint_main.svg?v=20", "blueprint_final.svg?v=1")
readme = readme.replace("blueprint_main.svg?v=19", "blueprint_final.svg?v=1")
readme = readme.replace("blueprint_main.svg?v=18", "blueprint_final.svg?v=1")
readme = readme.replace("blueprint_main.svg?v=17", "blueprint_final.svg?v=1")
readme = readme.replace("blueprint_main.svg?v=16", "blueprint_final.svg?v=1")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
