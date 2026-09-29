# ============================================================
#   BARA HACK TOOL - TIKTOK OSINT
#   Created by Bara
# ============================================================

import re
import requests
from ui import (section, err, info, field, end_field,
                prompt, press_enter, loading_bar)


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

    info(f"Username: @{username}")
    loading_bar("Fetching")

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0"}
    try:
        r = requests.get(f"https://www.tiktok.com/@{username}", headers=headers, timeout=10)
        if r.status_code != 200:
            err(f"HTTP {r.status_code}")
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
        print(f"\n")
        for label, pat in fields.items():
            m = re.search(pat, html)
            field(label, m.group(1) if m else "-")
        end_field()
    except Exception as e:
        err(f"Error: {e}")

    press_enter()
