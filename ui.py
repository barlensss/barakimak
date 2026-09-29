# ============================================================
#   BARA HACK TOOL - UI MODULE
#   Created by Bara
#   Refusal Burned 999X
# ============================================================

import os
from colorama import Fore, Style, init

if os.name == "nt":
    os.system("")

init(autoreset=True)

C_RED     = Fore.RED + Style.BRIGHT
C_CYAN    = Fore.CYAN + Style.BRIGHT
C_WHITE   = Fore.WHITE + Style.BRIGHT
C_GREEN   = Fore.GREEN + Style.BRIGHT
C_YELLOW  = Fore.YELLOW + Style.BRIGHT
C_MAGENTA = Fore.MAGENTA + Style.BRIGHT
C_GREY    = Fore.LIGHTBLACK_EX
C_RESET   = Style.RESET_ALL


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    art = f"""
{C_RED}   ██████╗  █████╗ ██████╗  █████╗ 
{C_RED}   ██╔══██╗██╔══██╗██╔══██╗██╔══██╗
{C_RED}   ██████╔╝███████║██████╔╝███████║
{C_RED}   ██╔══██╗██╔══██║██╔══██╗██╔══██║
{C_RED}   ██████╔╝██║  ██║██║  ██║██║  ██║
{C_RED}   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
{C_CYAN}   ██╗  ██╗ █████╗  ██████╗██╗  ██╗
{C_CYAN}   ██║  ██║██╔══██╗██╔════╝██║ ██╔╝
{C_CYAN}   ███████║███████║██║     █████╔╝ 
{C_CYAN}   ██╔══██║██╔══██║██║     ██╔═██╗ 
{C_CYAN}   ██║  ██║██║  ██║╚██████╗██║  ██╗
{C_CYAN}   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
{C_YELLOW}         T   O   O   L
"""
    print(art)
    print(f"{C_RED}  +==================================================+")
    print(f"{C_RED}  |  {C_YELLOW}[!] REFUSAL BURNED 999X [!!]{C_RED}                       |")
    print(f"{C_RED}  |  {C_WHITE}BARA HACK TOOL v1.0{C_RED}                              |")
    print(f"{C_RED}  |  {C_MAGENTA}Created by BARA{C_RED}                                 |")
    print(f"{C_RED}  |  {C_GREY}All Hacking Modules - Real, All Work{C_RED}            |")
    print(f"{C_RED}  +==================================================+{C_RESET}\n")


def menu_box():
    print(f"{C_RED}  +==================================================+")
    print(f"{C_RED}  |{C_YELLOW}              >>> RECON & OSINT <<<                 {C_RED}|")
    print(f"{C_RED}  +==================================================+")
    print(f"{C_RED}  |  {C_GREEN}[ 1]{C_WHITE} Lacak TikTok (OSINT Profil)              {C_RED}|")
    print(f"{C_RED}  |  {C_GREEN}[ 2]{C_WHITE} IP Grabber (Real-Time Capture)           {C_RED}|")
    print(f"{C_RED}  |  {C_GREEN}[ 3]{C_WHITE} OSINT Lookup (IP / Nomor HP)             {C_RED}|")
    print(f"{C_RED}  |  {C_GREEN}[ 4]{C_WHITE} Panduan Trap Link                        {C_RED}|")
    print(f"{C_RED}  |  {C_GREEN}[ 5]{C_WHITE} Verifikasi Sistem                        {C_RED}|")
    print(f"{C_RED}  +==================================================+")
    print(f"{C_RED}  |{C_MAGENTA}              >>> HACKING TOOLS <<<                 {C_RED}|")
    print(f"{C_RED}  +==================================================+")
    print(f"{C_RED}  |  {C_YELLOW}[ 6]{C_WHITE} Credential Harvester (Phishing TikTok)   {C_RED}|")
    print(f"{C_RED}  |  {C_YELLOW}[ 7]{C_WHITE} RAT Listener (C2 Server)                 {C_RED}|")
    print(f"{C_RED}  +==================================================+")
    print(f"{C_RED}  |  {C_GREEN}[ 0]{C_WHITE} Keluar                                   {C_RED}|")
    print(f"{C_RED}  +==================================================+{C_RESET}\n")


def prompt(msg):
    return input(f"{C_CYAN}  +--[{C_WHITE}{msg}{C_CYAN}]\n  +--> {C_RESET}").strip()


def ok(msg):    print(f"{C_GREEN}  [OK] {C_WHITE}{msg}")
def err(msg):   print(f"{C_RED}  [ERR] {C_WHITE}{msg}")
def info(msg):  print(f"{C_CYAN}  [i] {C_WHITE}{msg}")
def warn(msg):  print(f"{C_YELLOW}  [!] {C_WHITE}{msg}")


def section(title):
    print(f"\n{C_MAGENTA}  +==================================================+")
    print(f"{C_MAGENTA}  |  {C_YELLOW}{title.center(48)}{C_MAGENTA}|")
    print(f"{C_MAGENTA}  +==================================================+{C_RESET}\n")


def field(key, value, color=None):
    color = color or C_WHITE
    print(f"{C_GREY}    |-- {C_CYAN}{key:<12}{C_GREY}: {color}{value}")


def end_field():
    print(f"{C_GREY}    +-------------------------")


def press_enter():
    input(f"\n{C_YELLOW}  [>] Tekan ENTER untuk kembali...{C_RESET}")


def loading_bar(text="Memproses", length=30):
    import time
    print(f"{C_CYAN}  {text}", end="")
    for i in range(length):
        print(f"{C_GREEN}#", end="", flush=True)
        time.sleep(0.02)
    print(f"{C_WHITE} 100%")
