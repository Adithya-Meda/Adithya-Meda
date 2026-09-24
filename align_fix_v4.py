with open("build.py", "r", encoding="utf-8") as f:
    build = f.read()

# Strip out the broken hardcoded README writer at the bottom
build = build.split("import build")[0]

# Add a proper, dynamic README writer that points to blueprint_final.svg
proper_readme_writer = """
    import time
    v = int(time.time())
    
    readme = f'''<div align="center">
<img src="./assets/blueprint_final.svg?v={v}" style="display: block; margin: 0; padding: 0; border: none; outline: none;" />

<!-- INTERACTIVE DEPLOYMENTS (REPO CARDS) -->
<a href="https://github.com/Adithya-Meda/wisebiz-ecommerce-app"><img src="./assets/repo_wisebiz-ecommerce-app.svg?v={v}" alt="AWS Landing Zone Resource" style="vertical-align: top;"></a><a href="https://github.com/Adithya-Meda/wisebiz-gitops"><img src="./assets/repo_wisebiz-gitops.svg?v={v}" alt="K8s GitOps Resource" style="vertical-align: top;"></a>
<a href="https://github.com/Adithya-Meda/wisebiz-terraform"><img src="./assets/repo_wisebiz-terraform.svg?v={v}" alt="Wisebiz Terraform Resource" style="display: block;"></a>
</div>
'''

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)
"""

build = build + proper_readme_writer

with open("build.py", "w", encoding="utf-8") as f:
    f.write(build)

import os
os.system("python build.py")
