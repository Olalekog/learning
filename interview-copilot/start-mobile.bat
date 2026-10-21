@echo off
setlocal
cd /d "%~dp0"
title Interview Copilot - phone link

rem ---- 1. Python environment (first run only) ----
if not exist ".venv\Scripts\python.exe" (
  echo Setting up for first run...
  python -m venv .venv
  ".venv\Scripts\python.exe" -m pip install -q -r requirements.txt
)

rem ---- 2. API key ----
if "%ANTHROPIC_API_KEY%"=="" (
  set /p ANTHROPIC_API_KEY=Paste your Anthropic API key and press Enter:
)

rem ---- 3. Access code (made once, saved in access-code.txt) ----
if not exist "access-code.txt" (
  powershell -NoProfile -Command "-join ([char[]]'ABCDEFGHJKLMNPQRSTUVWXYZ23456789' | Get-Random -Count 10)" > access-code.txt
)
set /p ACCESS_CODE=<access-code.txt

rem ---- 4. Cloudflare Tunnel (gives a secure https link that works on mobile data too) ----
rem (no if-blocks here: the ")" in "Program Files (x86)" breaks them)
set "CF_A=%ProgramFiles(x86)%\cloudflared\cloudflared.exe"
set "CF_B=%ProgramFiles%\cloudflared\cloudflared.exe"
set "TRIED_INSTALL="
:findcf
set "CF="
where cloudflared >nul 2>nul && set "CF=cloudflared"
if not defined CF if exist "%CF_A%" set "CF=%CF_A%"
if not defined CF if exist "%CF_B%" set "CF=%CF_B%"
if defined CF goto havecf
if defined TRIED_INSTALL goto nocf
echo cloudflared is not installed. Installing it with winget...
winget install --id Cloudflare.cloudflared -e --accept-source-agreements --accept-package-agreements
set "TRIED_INSTALL=1"
goto findcf
:nocf
echo.
echo Could not find cloudflared after installing. Close this window and run start-mobile.bat again.
pause
exit /b 1
:havecf

rem ---- 5. Start the server in its own window ----
start "Interview Copilot server" ".venv\Scripts\python.exe" server.py

echo.
echo  ==============================================================
echo   On your phone:
echo   1. Wait for a line below like  https://something.trycloudflare.com
echo   2. Open that link in Chrome (Android) or Safari (iPhone)
echo   3. Enter this access code:   %ACCESS_CODE%
echo.
echo   The link changes every time you run this. Close this window
echo   and the server window to stop.
echo  ==============================================================
echo.
"%CF%" tunnel --no-autoupdate --url http://localhost:8765
