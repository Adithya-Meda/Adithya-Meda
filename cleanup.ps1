# Remove old python/temp files
Remove-Item -Path "old_build.py", "original_build.py", "prep.py", "temp_top.svg" -ErrorAction SilentlyContinue

# Remove old SVG assets
Remove-Item -Path "assets/blueprint_final.svg", "assets/blueprint_main.svg" -ErrorAction SilentlyContinue
Remove-Item -Path "assets/repo_wisebiz-ecommerce-app.svg", "assets/repo_wisebiz-gitops.svg", "assets/repo_wisebiz-terraform.svg" -ErrorAction SilentlyContinue

git add .
git commit -m "chore: clean up obsolete scripts and cached SVG assets"
git push origin main
