@echo off
echo ========================================================
echo Pushing Snagged updates to GitHub (vyassoham/snagged)
echo ========================================================
echo.

git add .
git commit -m "Site update" 2>nul
git push origin main

echo.
echo Push complete! Vercel will automatically deploy your updates.
pause
