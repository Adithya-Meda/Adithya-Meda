with open("build.py", "r", encoding="utf-8") as f:
    build = f.read()

# Fix the README generation at the bottom of build.py
new_readme_logic = """
readme = '<div align="center">\\n'
readme += '<img src="./assets/blueprint_main.svg?v=16" style="display: block; margin: 0; padding: 0; border: none; outline: none;" />\\n'
readme += '''
<!-- INTERACTIVE DEPLOYMENTS (REPO CARDS) -->
<a href="https://github.com/Adithya-Meda/wisebiz-ecommerce-app"><img src="./assets/repo_wisebiz-ecommerce-app.svg?v=16" alt="AWS Landing Zone Resource" style="vertical-align: top;"></a><a href="https://github.com/Adithya-Meda/wisebiz-gitops"><img src="./assets/repo_wisebiz-gitops.svg?v=16" alt="K8s GitOps Resource" style="vertical-align: top;"></a>
<a href="https://github.com/Adithya-Meda/wisebiz-terraform"><img src="./assets/repo_wisebiz-terraform.svg?v=16" alt="Wisebiz Terraform Resource" style="display: block;"></a>
</div>
'''

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
"""

# Replace the end part of build.py
import re
build = re.sub(r'readme = \'<div align="center">\\n\'.*?f\.write\(readme\)', new_readme_logic, build, flags=re.DOTALL)

with open("build.py", "w", encoding="utf-8") as f:
    f.write(build)

import os
os.system("python build.py")
