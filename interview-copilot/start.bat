@echo off
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Setting up for first run...
  python -m venv .venv
  ".venv\Scripts\python.exe" -m pip install -q -r requirements.txt
)
if "%ANTHROPIC_API_KEY%"=="" (
  set /p ANTHROPIC_API_KEY=Paste your Anthropic API key and press Enter: 
)
start "" http://localhost:8765
".venv\Scripts\python.exe" server.py
