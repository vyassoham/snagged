@echo off
echo ========================================================
echo Snagged - Vercel Deployment Script (Zero Cost Hosting)
echo ========================================================
echo.
echo Make sure you have Node.js installed.
echo Press any key to install Vercel CLI (if not installed) and deploy...
pause

call npm install -g vercel

echo.
echo ========================================================
echo Step 1: Vercel will ask you to log in (opens browser).
echo Step 2: It will ask to set up and deploy (Type Y).
echo Step 3: Which scope do you want to deploy to? (Hit Enter)
echo Step 4: Link to existing project? (Type N)
echo Step 5: What's your project's name? (Type: snagged-store)
echo Step 6: In which directory is your code? (Type: ./website)
echo ========================================================
echo.

call vercel --prod
echo.
echo Deployment Complete! Your site is live.
pause
