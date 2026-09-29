# ============================================================
#   UNITED AI TOOLKIT - WINDOWS INSTALLER
#   Made by Nyxveil - Continued by Tebo Yang Mulia
# ============================================================

$ErrorActionPreference = "Continue"
$Host.UI.RawUI.WindowTitle = "United AI Toolkit - Installer"

# ============ WARNA & UI ============
function Write-Banner {
    Clear-Host
    Write-Host ""
    Write-Host "   ██╗   ██╗███╗   ██╗██╗████████╗███████╗██████╗ " -ForegroundColor Red
    Write-Host "   ██║   ██║████╗  ██║██║╚══██╔══╝██╔════╝██╔══██╗" -ForegroundColor Red
    Write-Host "   ██║   ██║██╔██╗ ██║██║   ██║   █████╗  ██║  ██║" -ForegroundColor Red
    Write-Host "   ██║   ██║██║╚██╗██║██║   ██║   ██╔══╝  ██║  ██║" -ForegroundColor Red
    Write-Host "   ╚██████╔╝██║ ╚████║██║   ██║   ███████╗██████╔╝" -ForegroundColor Red
    Write-Host "    ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚══════╝╚═════╝ " -ForegroundColor Red
    Write-Host "              █████╗ ██╗" -ForegroundColor Cyan
    Write-Host "             ██╔══██╗██║" -ForegroundColor Cyan
    Write-Host "             ███████║██║" -ForegroundColor Cyan
    Write-Host "             ██╔══██║██║" -ForegroundColor Cyan
    Write-Host "             ██║  ██║██║" -ForegroundColor Cyan
    Write-Host "             ╚═╝  ╚═╝╚═╝" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "  +==================================================+" -ForegroundColor Red
    Write-Host "  |  [!!] REFUSAL BURNED 999X [!!]                    |" -ForegroundColor Yellow
    Write-Host "  |  United AI Toolkit v9.7.3 - Windows Installer    |" -ForegroundColor White
    Write-Host "  |  Made by Nyxveil -> Tebo Yang Mulia              |" -ForegroundColor DarkGray
    Write-Host "  +==================================================+" -ForegroundColor Red
    Write-Host ""
}

function Write-Step   ($msg) { Write-Host "  [*] $msg" -ForegroundColor Yellow }
function Write-Ok     ($msg) { Write-Host "  [OK] $msg" -ForegroundColor Green }
function Write-Fail   ($msg) { Write-Host "  [ERR] $msg" -ForegroundColor Red }
function Write-Info   ($msg) { Write-Host "  [i] $msg" -ForegroundColor Cyan }
function Write-Warn   ($msg) { Write-Host "  [!] $msg" -ForegroundColor Magenta }

# ============ MULAI ============
Write-Banner

Write-Info "Installer ini akan menyiapkan environment untuk United AI Toolkit."
Write-Info "Pastikan kamu terhubung ke internet."
Write-Host ""
Read-Host "  [>] Tekan ENTER untuk mulai install"

Write-Host ""
Write-Host "  ==============================================" -ForegroundColor DarkGray
Write-Host "   STEP 1 / 6 : CEK PYTHON" -ForegroundColor Cyan
Write-Host "  ==============================================" -ForegroundColor DarkGray

Write-Step "Cek Python..."
$pythonCmd = $null
if (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCmd = "python"
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCmd = "py"
}

if (-not $pythonCmd) {
    Write-Fail "Python TIDAK ditemukan."
    Write-Host ""
    Write-Warn "Silakan install Python dari: https://www.python.org/downloads/"
    Write-Warn "PENTING: centang 'Add Python to PATH' saat install!"
    Write-Host ""
    Write-Info "Setelah install, RESTART PowerShell lalu jalankan installer ini lagi."
    Read-Host "  [>] Tekan ENTER untuk keluar"
    exit 1
}

$pyVersion = & $pythonCmd --version 2>&1
Write-Ok "Python ditemukan: $pyVersion"

# Cek versi minimal 3.8
$verStr = ($pyVersion -replace "Python ", "").Trim()
$verParts = $verStr.Split(".")
$major = [int]$verParts[0]
$minor = [int]$verParts[1]
if ($major -lt 3 -or ($major -eq 3 -and $minor -lt 8)) {
    Write-Fail "Python versi $verStr terlalu lama. Butuh minimal 3.8+"
    Read-Host "  [>] Tekan ENTER untuk keluar"
    exit 1
}

Write-Host ""
Write-Host "  ==============================================" -ForegroundColor DarkGray
Write-Host "   STEP 2 / 6 : CEK PIP" -ForegroundColor Cyan
Write-Host "  ==============================================" -ForegroundColor DarkGray

Write-Step "Cek pip..."
try {
    $pipVer = & $pythonCmd -m pip --version 2>&1
    Write-Ok "pip tersedia: $pipVer"
} catch {
    Write-Fail "pip tidak tersedia. Mencoba install..."
    & $pythonCmd -m ensurepip --upgrade
}

Write-Host ""
Write-Host "  ==============================================" -ForegroundColor DarkGray
Write-Host "   STEP 3 / 6 : UPDATE PIP" -ForegroundColor Cyan
Write-Host "  ==============================================" -ForegroundColor DarkGray

Write-Step "Upgrade pip ke versi terbaru..."
& $pythonCmd -m pip install --upgrade pip --quiet
Write-Ok "Pip sudah update"

Write-Host ""
Write-Host "  ==============================================" -ForegroundColor DarkGray
Write-Host "   STEP 4 / 6 : INSTALL DEPENDENCIES" -ForegroundColor Cyan
Write-Host "  ==============================================" -ForegroundColor DarkGray

$deps = @("requests", "colorama", "phonenumbers")
foreach ($dep in $deps) {
    Write-Step "Install: $dep"
    & $pythonCmd -m pip install $dep --quiet
    if ($LASTEXITCODE -eq 0) {
        Write-Ok "$dep terinstall"
    } else {
        Write-Fail "$dep gagal install"
    }
}

Write-Host ""
Write-Host "  ==============================================" -ForegroundColor DarkGray
Write-Host "   STEP 5 / 6 : CEK CLOUDFLARED" -ForegroundColor Cyan
Write-Host "  ==============================================" -ForegroundColor DarkGray

Write-Step "Cek cloudflared (untuk tunnel IP Grabber)..."
if (Get-Command cloudflared -ErrorAction SilentlyContinue) {
    $cfVer = cloudflared --version 2>&1
    Write-Ok "cloudflared terinstall: $cfVer"
} else {
    Write-Warn "cloudflared TIDAK ditemukan."
    Write-Info "cloudflared dibutuhkan untuk fitur IP Grabber (tunnel)."
    Write-Host ""
    $answer = Read-Host "  [?] Install cloudflared sekarang via winget? (y/n)"

    if ($answer -eq "y" -or $answer -eq "Y") {
        if (Get-Command winget -ErrorAction SilentlyContinue) {
            Write-Step "Install cloudflared via winget..."
            winget install --id Cloudflare.cloudflared --accept-source-agreements --accept-package-agreements
            Write-Ok "cloudflared terinstall. RESTART PowerShell untuk pakai."
        } else {
            Write-Fail "winget tidak tersedia."
            Write-Info "Download manual: https://github.com/cloudflare/cloudflared/releases/latest"
            Write-Info "Ambil: cloudflared-windows-amd64.exe -> rename -> cloudflared.exe"
            Write-Info "Taruh di: C:\Windows\System32\"
        }
    } else {
        Write-Warn "Skip. IP Grabber butuh cloudflared untuk jalan."
    }
}

Write-Host ""
Write-Host "  ==============================================" -ForegroundColor DarkGray
Write-Host "   STEP 6 / 6 : AKTIFKAN ANSI (WARNA TERMINAL)" -ForegroundColor Cyan
Write-Host "  ==============================================" -ForegroundColor DarkGray

Write-Step "Aktifkan ANSI color di PowerShell..."
try {
    Set-ItemProperty -Path "HKCU:\Console" -Name "VirtualTerminalLevel" -Value 1 -ErrorAction Stop
    Write-Ok "ANSI aktif. Warna bakal muncul di terminal."
} catch {
    Write-Warn "Gagal set registry. Pakai Windows Terminal untuk hasil terbaik."
}

# ============ SELESAI ============
Write-Host ""
Write-Host "  +==================================================+" -ForegroundColor Green
Write-Host "  |              [OK] INSTALL SELESAI                |" -ForegroundColor Green
Write-Host "  +==================================================+" -ForegroundColor Green
Write-Host ""
Write-Host "  Cara pakai:" -ForegroundColor Cyan
Write-Host "    1. Jalankan: " -NoNewline -ForegroundColor White
Write-Host "python main.py" -ForegroundColor Yellow
Write-Host "    2. Atau double-click: " -NoNewline -ForegroundColor White
Write-Host "run.bat" -ForegroundColor Yellow
Write-Host ""
Write-Host "  Untuk grab IP target (2 PowerShell):" -ForegroundColor Cyan
Write-Host "    PS#1: python main.py  -> pilih [2]" -ForegroundColor White
Write-Host "    PS#2: cloudflared tunnel --url http://localhost:8080" -ForegroundColor White
Write-Host ""
Write-Host "  Made by Nyxveil - Continued by Tebo Yang Mulia" -ForegroundColor DarkGray
Write-Host ""

Read-Host "  [>] Tekan ENTER untuk keluar"
