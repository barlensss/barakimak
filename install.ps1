# united-ai | windows installer
# Made by Nyxveil - Continued by Tebo Yang Mulia

Write-Host "=== UNITED AI TOOLKIT — WINDOWS INSTALLER ===" -ForegroundColor Cyan

# Cek Python
Write-Host "[*] Cek Python..." -ForegroundColor Yellow
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "[✗] Python tidak ditemukan. Install dari python.org dulu." -ForegroundColor Red
    exit 1
}
python --version

# Cek Git
Write-Host "[*] Cek Git..." -ForegroundColor Yellow
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "[!] Git tidak ditemukan — tidak wajib, tapi disarankan." -ForegroundColor Yellow
} else {
    git --version
}

# Cek Cloudflared
Write-Host "[*] Cek cloudflared..." -ForegroundColor Yellow
if (-not (Get-Command cloudflared -ErrorAction SilentlyContinue)) {
    Write-Host "[!] cloudflared tidak ditemukan. Install: winget install --id Cloudflare.cloudflared" -ForegroundColor Yellow
} else {
    cloudflared --version
}

# Aktifkan ANSI
Write-Host "[*] Aktifkan ANSI di PowerShell..." -ForegroundColor Yellow
Set-ItemProperty -Path "HKCU:\Console" -Name "VirtualTerminalLevel" -Value 1

# Install dependencies
Write-Host "[*] Install Python packages..." -ForegroundColor Yellow
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

Write-Host ""
Write-Host "[✓] INSTALL SELESAI" -ForegroundColor Green
Write-Host "[>] Jalankan: python main.py" -ForegroundColor Cyan
Write-Host "[>] Atau klik: run.bat" -ForegroundColor Cyan
