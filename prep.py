import os
import html

with open("original_build.py", "r", encoding="utf-8") as f:
    build_py = f.read()

# 1. Fix margins in blueprint_header
build_py = build_py.replace('<svg width="800" height="280"', '<svg width="800" height="245"')
build_py = build_py.replace('<rect x="20" y="20" width="760" height="240"', '<rect x="20" y="2" width="760" height="240"')
# Move contents up by 18px
build_py = build_py.replace('y="10"', 'y="-8"')
build_py = build_py.replace('y="25"', 'y="7"')
build_py = build_py.replace('transform="translate(0, 40)"', 'transform="translate(0, 22)"')

# 2. Fix margins in blueprint_philosophy
build_py = build_py.replace('<svg width="800" height="180"', '<svg width="800" height="145"')
build_py = build_py.replace('<rect x="20" y="20" width="760" height="140"', '<rect x="20" y="2" width="760" height="140"')
build_py = build_py.replace('y="45"', 'y="27"')
build_py = build_py.replace('transform="translate(40, 80)"', 'transform="translate(40, 62)"')

# 3. Fix margins in blueprint_dns_header
build_py = build_py.replace('<svg width="800" height="80"', '<svg width="800" height="50"')
build_py = build_py.replace('y="35"', 'y="15"')
build_py = build_py.replace('y1="50"', 'y1="30"')
build_py = build_py.replace('y2="50"', 'y2="30"')
build_py = build_py.replace('y="70"', 'y="45"')

# 4. Fix margins in blueprint_dns_socials (the rows)
# Wait, original_build.py didn't have generate_dns_rows() split, it had generate_dns_socials() which might be separate or together?
# Let's check how it was written in original_build.py
