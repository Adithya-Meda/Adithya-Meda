with open("build.py", "r", encoding="utf-8") as f:
    build = f.read()

# Replace first static circle with animated one
build = build.replace(
    '<circle cx="210" cy="80" r="4" fill="#ffffff" filter="url(#drop-shadow)"/>',
    '<circle r="4" fill="#ffffff" filter="url(#neon-glow)"><animateMotion dur="2s" repeatCount="indefinite"><mpath href="#data-path"/></animateMotion></circle>'
)

# Replace second static circle with animated one (reverse direction if needed, but original had keyPoints="1;0")
build = build.replace(
    '<circle cx="615" cy="80" r="4" fill="#ffffff" filter="url(#drop-shadow)"/>',
    '<circle r="4" fill="#ffffff" filter="url(#neon-glow)"><animateMotion dur="2.5s" repeatCount="indefinite" keyPoints="1;0" keyTimes="0;1" calcMode="linear"><mpath href="#data-path-out"/></animateMotion></circle>'
)

with open("build.py", "w", encoding="utf-8") as f:
    f.write(build)

import os
os.system("python build.py")
