# united-ai | verification module
# Made by Nyxveil - Continued by Tebo Yang Mulia

import requests
from ui import ok, err, warn, info, section, C_GREEN, C_RED, C_YELLOW, C_WHITE

CHECKS = {
    "IPinfo API":       "https://ipinfo.io/8.8.8.8/json",
    "IP-API":           "http://ip-api.com/json/8.8.8.8",
    "Cloudflare Trace": "https://www.cloudflare.com/cdn-cgi/trace",
    "TikTok Public":    "https://www.tiktok.com/@tiktok",
    "Internet":         "https://1.1.1.1",
}

def check(name, url):
    try:
        r = requests.get(url, timeout=8)
        if r.status_code < 400:
            print(f"{C_GREEN}  [OK]  {C_WHITE}{name:<20} {C_GREEN}ONLINE")
            return "ON"
        print(f"{C_YELLOW}  [!]   {C_WHITE}{name:<20} {C_YELLOW}HTTP {r.status_code}")
        return "ERR"
    except Exception as e:
        print(f"{C_RED}  [ERR] {C_WHITE}{name:<20} {C_RED}OFFLINE ({type(e).__name__})")
        return "OFF"

def get_my_public_ip():
    try:
        return requests.get("https://api.ipify.org", timeout=5).text.strip()
    except Exception:
        return None

def verify_all():
    section("VERIFIKASI SISTEM")
    results = {}
    for name, url in CHECKS.items():
        results[name] = check(name, url)
    all_on = all(v == "ON" for v in results.values())
    print()
    my_ip = get_my_public_ip()
    if my_ip:
        info(f"IP publik kamu: {my_ip}")
    if all_on:
        print(f"\n{C_GREEN}  >>> SEMUA SISTEM ON - SIAP TEMPUR <<<\n")
    else:
        print(f"\n{C_YELLOW}  >>> ADA ERROR - TAPI TETAP LANJUT <<<\n")
    return all_on

if __name__ == "__main__":
    verify_all()
