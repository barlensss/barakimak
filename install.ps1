# ============================================================
#   BARA HACK TOOL - WINDOWS INSTALLER
#   Created by Bara
# ============================================================

$ErrorActionPreference = "Continue"
$Host.UI.RawUI.WindowTitle = "BARA HACK TOOL - Installer"

function Write-Banner {
    Clear-Host
    Write-Host ""
    Write-Host "   ██████╗  █████╗ ██████╗  █████╗ " -ForegroundColor Red
    Write-Host "   ██╔══██╗██╔══██╗██╔══██╗██╔══██╗" -ForegroundColor Red
    Write-Host "   ██████╔╝███████║██████╔╝███████║" -ForegroundColor Red
    Write-Host "   ██╔══██╗██╔══██║██╔══██╗██╔══██║" -ForegroundColor Red
    Write-Host "   ██████╔╝██║  ██║██║  ██║██║  ██║" -ForegroundColor Red
    Write-Host "   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝" -ForegroundColor Red
    Write-Host "   ██╗  ██╗ █████╗  ██████╗██╗  ██╗" -ForegroundColor Cyan
    Write-Host "   ██║  ██║██╔══██╗██╔════╝██║ ██╔╝" -ForegroundColor Cyan
    Write-Host "   ███████║███████║██║     █████╔╝ " -ForegroundColor Cyan
    Write-Host "   ██╔══██║██╔══██║██║     ██╔═██╗ " -ForegroundColor Cyan
    Write-Host "   ██║  ██║██║  ██║╚██████╗██║  ██╗" -ForegroundColor Cyan
    Write-Host "   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝" -ForegroundColor Cyan
    Write-Host "         T   O   O   L" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "  +==================================================+" -ForegroundColor Red
    Write-Host "  |  [!!] REFUSAL BURNED 999X [!!]                    |" -ForegroundColor Yellow
    Write-Host "  |  BARA HACK TOOL v1.0                              |" -ForegroundColor White
    Write-Host "  |  Created by BARA                                  |" -ForegroundColor Magenta
    Write-Host "  +==================================================+" -ForegroundColor Red
    Write-Host ""
}

function Write-Step ($msg) { Write-Host "  [*] $msg" -ForegroundColor Yellow }
function Write-Ok   ($msg) { Write-Host "  [OK] $msg" -ForegroundColor Green }
function Write-Fail ($msg) { Write-Host "  [ERR] $msg" -ForegroundColor Red }
function Write-Info ($msg) { Write-Host "  [i] $msg" -ForegroundColor Cyan }
function Write-Warn ($msg) { Write-Host "  [!] $msg" -ForegroundColor Magenta }

Write-Banner
Write-Info "Installer ini akan siapkan environment BARA HACK TOOL."
Read-Host "  [>] Tekan ENTER untuk mulai install"

# STEP 1 - Python
Write-Host ""
Write-Host "  ==============================================" -ForegroundColor DarkGray
Write-Host "   STEP 1 / 5 : CEK PYTHON" -ForegroundColor Cyan
Write-Host "  ==============================================" -ForegroundColor DarkGray

Write-Step "Cek Python..."
$pythonCmd = $null
if (Get-Command python -ErrorAction SilentlyContinue) { $pythonCmd = "python" }
elseif (Get-Command py -ErrorAction SilentlyContinue) { $pythonCmd = "py" }

if (-not $pythonCmd) {
    Write-Fail "Python TIDAK ditemukan."
    Write-Warn "Install dari: https://www.python.org/downloads/"
    Write-Warn "Centang 'Add Python to PATH'!"
    Read-Host "  [>] ENTER untuk keluar"
    exit 1
}
$pyVersion = & $pythonCmd --version 2>&1
Write-Ok "Python: $pyVersion"

# STEP 2 - pip
Write-Host ""
Write-Host "  ==============================================" -ForegroundColor DarkGray
Write-Host "   STEP 2 / 5 : CEK PIP" -ForegroundColor Cyan
Write-Host "  ==============================================" -ForegroundColor DarkGray
Write-Step "Cek pip..."
try {
    & $pythonCmd -m pip --version | Out-Null
    Write-Ok "pip OK"
} catch {
    & $pythonCmd -m ensurepip --upgrade
}

# STEP 3 - Dependencies
Write-Host ""
Write-Host "  ==============================================" -ForegroundColor DarkGray
Write-Host "   STEP 3 / 5 : INSTALL DEPENDENCIES" -ForegroundColor Cyan
Write-Host "  ==============================================" -ForegroundColor DarkGray
& $pythonCmd -m pip install --upgrade pip --quiet
foreach ($dep in @("requests", "colorama", "phonenumbers")) {
    Write-Step "Install: $dep"
    & $pythonCmd -m pip install $dep --quiet
    Write-Ok "$dep"
}

# STEP 4 - cloudflared
Write-Host ""
Write-Host "  ==============================================" -ForegroundColor DarkGray
Write-Host "   STEP 4 / 5 : CLOUDFLARED" -ForegroundColor Cyan
Write-Host "  ==============================================" -ForegroundColor DarkGray
if (Get-Command cloudflared -ErrorAction SilentlyContinue) {
    Write-Ok "cloudflared terinstall"
} else {
    Write-Warn "cloudflared belum ada."
    $ans = Read-Host "  [?] Install via winget? (y/n)"
    if ($ans -match "^[Yy]$" -and (Get-Command winget -ErrorAction SilentlyContinue)) {
        winget install --id Cloudflare.cloudflared --accept-source-agreements --accept-package-agreements
    } else {
        Write-Info "Download manual: https://github.com/cloudflare/cloudflared/releases/latest"
    }
}

# STEP 5 - ANSI
Write-Host ""
Write-Host "  ==============================================" -ForegroundColor DarkGray
Write-Host "   STEP 5 / 5 : AKTIFKAN ANSI" -ForegroundColor Cyan
Write-Host "  ==============================================" -ForegroundColor DarkGray
try {
    Set-ItemProperty -Path "HKCU:\Console" -Name "VirtualTerminalLevel" -Value 1 -ErrorAction Stop
    Write-Ok "ANSI aktif"
} catch {
    Write-Warn "Gagal set registry. Pakai Windows Terminal."
}

Write-Host ""
Write-Host "  +==================================================+" -ForegroundColor Green
Write-Host "  |              [OK] INSTALL SELESAI                |" -ForegroundColor Green
Write-Host "  +==================================================+" -ForegroundColor Green
Write-Host ""
Write-Host "  Jalankan: python main.py" -ForegroundColor Yellow
Write-Host "  Atau   : run.bat" -ForegroundColor Yellow
Write-Host ""
Write-Host "  Created by BARA" -ForegroundColor DarkGray
Read-Host "  [>] ENTER untuk keluar"
