# ============================================================
#   BARA HACK TOOL - OSINT LOOKUP
#   Created by Bara
# ============================================================

import requests
from ui import (section, err, field, end_field,
                prompt, press_enter, loading_bar, C_WHITE, C_YELLOW)


def lookup_ip():
    section("OSINT - IP LOOKUP")
    ip = prompt("IP address")
    if not ip:
        err("Kosong.")
        press_enter()
        return
    loading_bar("Query")
    try:
        r = requests.get(
            f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,zip,lat,lon,isp,org,as,query,timezone",
            timeout=10
        ).json()
        if r.get("status") == "success":
            print(f"\n")
            for k, v in r.items():
                field(k, v)
            end_field()
        else:
            err("Gagal.")
    except Exception as e:
        err(f"Error: {e}")
    press_enter()


def lookup_phone():
    section("OSINT - PHONE")
    num = prompt("Nomor (+62812...)")
    if not num:
        err("Kosong.")
        press_enter()
        return
    loading_bar("Query")
    try:
        import phonenumbers
        from phonenumbers import geocoder, carrier, timezone
        p = phonenumbers.parse(num, None)
        print(f"\n")
        field("Country",  geocoder.description_for_number(p, "en"))
        field("Carrier",  carrier.name_for_number(p, "en"))
        field("Timezone", str(timezone.time_zones_for_number(p)))
        field("Valid",    str(phonenumbers.is_valid_number(p)))
        end_field()
    except Exception as e:
        err(f"Error: {e}")
    press_enter()


def osint_menu():
    section("OSINT LOOKUP")
    print(f"  {C_YELLOW}[1]{C_WHITE} IP")
    print(f"  {C_YELLOW}[2]{C_WHITE} Phone\n")
    sub = prompt("Pilih")
    if sub == "1": lookup_ip()
    elif sub == "2": lookup_phone()
    else:
        err("Invalid.")
        press_enter()
