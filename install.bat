@echo off
title BARA HACK TOOL - Installer
color 0C
cd /d "%~dp0"

echo.
echo   ============================================
echo    BARA HACK TOOL - INSTALLER
echo    Created by BARA
echo   ============================================
echo.

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0install.ps1"
pause
