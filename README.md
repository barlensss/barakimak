<div align="center">

```
   ██╗   ██╗███╗   ██╗██╗████████╗███████╗██████╗ 
   ██║   ██║████╗  ██║██║╚══██╔══╝██╔════╝██╔══██╗
   ██║   ██║██╔██╗ ██║██║   ██║   █████╗  ██║  ██║
   ██║   ██║██║╚██╗██║██║   ██║   ██╔══╝  ██║  ██║
   ╚██████╔╝██║ ╚████║██║   ██║   ███████╗██████╔╝
    ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚══════╝╚═════╝ 
              █████╗ ██╗
             ██╔══██╗██║
             ███████║██║
             ██╔══██║██║
             ██║  ██║██║
             ╚═╝  ╚═╝╚═╝
```

# 🔥 United AI Toolkit

**Terminal OSINT & IP Grabber — Windows Edition**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://microsoft.com/windows)
[![License](https://img.shields.io/badge/License-Educational-red?style=for-the-badge)](LICENSE)
[![Made By](https://img.shields.io/badge/Made%20By-Nyxveil-red?style=for-the-badge)](https://github.com)
[![Continued By](https://img.shields.io/badge/Continued%20By-Tebo%20Yang%20Mulia-gold?style=for-the-badge)](https://github.com)

> 🔥 **REFUSAL BURNED 999X** — Toolkit terminal untuk OSINT, IP tracking, dan TikTok profile intel.

</div>

---

## 📖 Daftar Isi

- [Fitur](#-fitur)
- [Preview](#-preview)
- [Instalasi Cepat](#-instalasi-cepat)
- [Instalasi Manual](#-instalasi-manual)
- [Cara Pakai](#-cara-pakai)
- [Cara Grab IP Target](#-cara-grab-ip-target-real-work)
- [Struktur Folder](#-struktur-folder)
- [Troubleshooting](#-troubleshooting)
- [FAQ](#-faq)
- [Disclaimer](#-disclaimer)

---

## ✨ Fitur

| # | Fitur | Deskripsi | Status |
|:-:|-------|-----------|:------:|
| 1 | 🎯 **Lacak TikTok** | OSINT data publik profil — username, ID, region, bio, followers | ✅ |
| 2 | 📡 **IP Grabber** | Real-time capture IP + geo + device via trap link | ✅ |
| 3 | 🔍 **OSINT Lookup** | Query IP & nomor HP — negara, ISP, carrier, timezone | ✅ |
| 4 | 🔗 **Panduan Trap** | Step-by-step cara kirim link ke target | ✅ |
| 5 | ⚙️ **Verifikasi** | Cek semua API & koneksi sebelum tempur | ✅ |

---

## 🎨 Preview

```
  +==================================================+
  |                 >>> MAIN MENU <<<                |
  +==================================================+
  |  [1]  [>] Lacak TikTok (OSINT Profil)            |
  |  [2]  [>] IP Grabber (Real-Time Capture)         |
  |  [3]  [>] OSINT Lookup (IP / Nomor HP)           |
  |  [4]  [>] Panduan Trap Link                      |
  |  [5]  [>] Verifikasi Sistem                      |
  |  [0]  [>] Keluar                                 |
  +==================================================+
```

**Contoh hasil IP Grabber:**

```
  +==================================================+
  |  [!!] TARGET CAPTURED - REAL TIME [!!]           |
  +==================================================+

    |-- time       : 2026-01-15 22:14:03
    |-- ip         : 114.122.xxx.xxx
    |-- country    : Indonesia
    |-- region     : DKI Jakarta
    |-- city       : Jakarta
    |-- lat        : -6.2088
    |-- lon        : 106.8456
    |-- isp        : Telkomsel
    |-- user_agent : Mozilla/5.0 (Linux; Android 13; SM-A536E)
    |-- language   : id-ID,id;q=0.9,en;q=0.8
    +-------------------------
```

---

## ⚡ Instalasi Cepat

### Windows (PowerShell)

```powershell
# 1. Buka PowerShell
# 2. Clone repo
git clone https://github.com/USERNAME/united-ai-toolkit.git
cd united-ai-toolkit

# 3. Jalankan installer
.\install.bat
```

Setelah selesai:

```powershell
python main.py
```

Atau **double-click `run.bat`**.

---

## 🛠️ Instalasi Manual

Kalau installer otomatis gagal, ikuti step ini.

### Step 1 — Install Python

1. Download: https://www.python.org/downloads/
2. **PENTING:** centang **Add Python to PATH**
3. Test: `python --version`

### Step 2 — Install Git (opsional)

Download: https://git-scm.com/download/win

### Step 3 — Aktifkan ANSI

```powershell
Set-ItemProperty -Path "HKCU:\Console" -Name "VirtualTerminalLevel" -Value 1
```

### Step 4 — Install cloudflared

```powershell
winget install --id Cloudflare.cloudflared
```

Manual: https://github.com/cloudflare/cloudflared/releases/latest
- Ambil `cloudflared-windows-amd64.exe`
- Rename jadi `cloudflared.exe`
- Taruh di `C:\Windows\System32\`

### Step 5 — Clone & install

```powershell
git clone https://github.com/USERNAME/united-ai-toolkit.git
cd united-ai-toolkit
python -m pip install -r requirements.txt
```

### Step 6 — Jalankan

```powershell
python main.py
```

---

## 🎮 Cara Pakai

### Menu 1 — Lacak TikTok

```
1. Pilih [1]
2. Masukkan URL: https://www.tiktok.com/@username
3. Tunggu hasil: nickname, ID, region, bio, followers
```

### Menu 2 — IP Grabber (yang beneran work)

```
1. Pilih [2]
2. Masukkan port: 8080 (ENTER untuk default)
3. Server jalan — tunggu target klik
```

### Menu 3 — OSINT Lookup

```
1. Pilih [3] -> [1] IP atau [2] Phone
2. Input IP (contoh: 8.8.8.8) atau nomor (+62812...)
3. Hasil: negara, ISP, carrier, timezone
```

### Menu 4 — Panduan Trap Link

Halaman instruksi lengkap cara pakai IP Grabber.

### Menu 5 — Verifikasi

Cek semua API. Kalau semua **ONLINE** = siap tempur.

---

## 🎯 Cara Grab IP Target (REAL WORK)

**Butuh 2 PowerShell.**

### PowerShell #1 — Server

```powershell
python main.py
# Pilih [2]
# Port: 8080
# Biarkan jalan, jangan close
```

### PowerShell #2 — Tunnel

```powershell
cloudflared tunnel --url http://localhost:8080
```

**Output cloudflared:**

```
+-----------------------------------------------------------+
|  Your quick Tunnel has been created!                      |
|  https://xxx-yyy-zzz.trycloudflare.com                    |
+-----------------------------------------------------------+
```

### Kirim link ke target

```
Copy: https://xxx-yyy-zzz.trycloudflare.com
Kirim via WA / DM / Email / dll
```

### Target klik -> data masuk REAL-TIME di PowerShell #1

```
  +==================================================+
  |  [!!] TARGET CAPTURED - REAL TIME [!!]           |
  +==================================================+
    |-- ip         : 114.122.xxx.xxx
    |-- country    : Indonesia
    |-- city       : Jakarta
    |-- isp        : Telkomsel
    |-- user_agent : ...Android 13...
    +-------------------------
```

Data juga otomatis tersimpan di **`captured.json`**.

---

## 📁 Struktur Folder

```
united-ai-toolkit/
│
├── main.py
├── ui.py
├── verify.py
├── requirements.txt
├── install.ps1
├── install.bat
├── run.bat
├── README.md
│
└── modules/
    ├── __init__.py
    ├── tiktok_trace.py
    ├── ip_grabber.py
    └── osint_lookup.py
```

---

## 🔧 Troubleshooting

### ❌ Warna tidak muncul

**Fix:** Pakai **Windows Terminal** (gratis di Microsoft Store).

```powershell
Set-ItemProperty -Path "HKCU:\Console" -Name "VirtualTerminalLevel" -Value 1
```

### ❌ Emoji jadi kotak

**Fix:** Pakai Windows Terminal atau install **Nerd Font**.

### ❌ Port 8080 diblokir firewall

**Fix:**
1. Windows Defender -> Firewall -> Allow an app
2. Centang **Python**
3. Atau ganti port saat diminta (contoh: 9090)

### ❌ `python` tidak dikenali

**Fix:**
- Coba `py main.py`
- Install ulang Python, centang **Add to PATH**

### ❌ `cloudflared` tidak dikenali

```powershell
winget install --id Cloudflare.cloudflared
```
Restart PowerShell.

### ❌ Error `WinError 10048`

Port sudah dipakai. Ganti port lain.

### ❌ `UnicodeEncodeError`

```powershell
$env:PYTHONIOENCODING="utf-8"
python main.py
```

---

## ❓ FAQ

<details>
<summary><b>Bisa lacak IP target hanya dari URL TikTok?</b></summary>

**Tidak.** TikTok tidak expose IP di halaman publik. Yang bilang bisa = scam.

Untuk dapat IP target, WAJIB pakai **IP Grabber** — target harus klik link.
</details>

<details>
<summary><b>Kenapa IP target cuma nunjukin kota, bukan alamat rumah?</b></summary>

Karena IP publik hanya terdaftar sampai level **kota / ISP**, bukan GPS presisi.
</details>

<details>
<summary><b>Kalau target pakai VPN, tetap kelihatan?</b></summary>

Yang terekam IP VPN, bukan IP asli.
</details>

<details>
<summary><b>Cloudflared wajib?</b></summary>

Wajib kalau mau target di luar jaringan lokal. Kalau target di WiFi yang sama, bisa pakai IP lokal.
</details>

<details>
<summary><b>Data tersimpan di mana?</b></summary>

`captured.json` di root folder.
</details>

---

## ⚠️ Disclaimer

> **Educational Purposes Only.**
>
> Toolkit ini dibuat untuk **pembelajaran, penetration testing legal, dan riset OSINT**.
> Segala penyalahgunaan di luar tanggung jawab pembuat.
> Patuhi hukum yang berlaku di wilayahmu.

---

## 🏆 Credits

<div align="center">

**Original Creator:**

### 🔥 Nyxveil 🔥

**Continued By:**

### 👑 Tebo Yang Mulia 👑

*"Refusal burned 999x — no noise, only execution."*

---

**⭐ Kalau repo ini berguna, kasih bintang! ⭐**

</div>

---

<div align="center">

```
Made with ❤️ by Nyxveil — Continued by Tebo Yang Mulia
```

</div>
