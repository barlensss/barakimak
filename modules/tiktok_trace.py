# united-ai | tiktok osint
# Made by Nyxveil - Continued by Tebo Yang Mulia

import re
import requests
from ui import (section, ok, err, info, warn, field, end_field,
                prompt, press_enter, loading_bar, C_WHITE, C_CYAN, C_YELLOW)

def extract_username(url):
    m = re.search(r"tiktok\.com/@([\w\.\-]+)", url)
    return m.group(1) if m else None

def tiktok_osint():
    section("LACAK TIKTOK - OSINT")
    url = prompt("Masukkan URL TikTok")
    if not url:
        err("URL kosong.")
        press_enter()
        return

    username = extract_username(url)
    if not username:
        err("URL tidak valid. Contoh: https://www.tiktok.com/@username")
        press_enter()
        return

    info(f"Username terdeteksi: @{username}")
    loading_bar("Mengambil data")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0 Safari/537.36"
    }
    try:
        r = requests.get(f"https://www.tiktok.com/@{username}", headers=headers, timeout=10)
        if r.status_code != 200:
            err(f"Gagal akses profil. HTTP {r.status_code}")
            press_enter()
            return

        html = r.text
        fields = {
            "Nickname":  r'"nickname":"([^"]+)"',
            "User ID":   r'"id":"(\d+)"',
            "Region":    r'"region":"([^"]+)"',
            "Bio":       r'"signature":"([^"]*)"',
            "Followers": r'"followerCount":(\d+)',
            "Following": r'"followingCount":(\d+)',
            "Likes":     r'"heartCount":(\d+)',
            "Verified":  r'"verified":(true|false)',
        }

        print(f"\n{C_CYAN}  +==================================================+")
        print(f"{C_CYAN}  |  {C_YELLOW}HASIL PELACAKAN TIKTOK{C_CYAN}                            |")
        print(f"{C_CYAN}  +==================================================+\n")

        for label, pat in fields.items():
            m = re.search(pat, html)
            val = m.group(1) if m else "-"
            field(label, val)

        end_field()
        print(f"\n{C_YELLOW}  [!] Data di atas = data publik TikTok.")
        print(f"{C_YELLOW}  [!] Untuk IP + device -> gunakan menu [2] IP Grabber.\n")

    except Exception as e:
        err(f"Error: {e}")

    press_enter()
