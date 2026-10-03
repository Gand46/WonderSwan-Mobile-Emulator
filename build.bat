@echo off
setlocal
cd /d "%~dp0"
py -3 tools\build.py
if errorlevel 1 python tools\build.py
endlocal
