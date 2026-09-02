import sys
import urllib.parse

# Ensure UTF-8 output on Windows terminal
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def build_utm_url(base_url="https://getsnagged.in", source="instagram", medium="organic_reel", campaign="launch_wave1", content=None):
    params = {
        "utm_source": source,
        "utm_medium": medium,
        "utm_campaign": campaign,
    }
    if content:
        params["utm_content"] = content

    query_str = urllib.parse.urlencode(params)
    return f"{base_url}?{query_str}"

if __name__ == "__main__":
    print("=" * 60)
    print("SNAGGED™ UTM TRACKING LINK GENERATOR")
    print("=" * 60)
    
    links = [
        ("Instagram Bio Link", build_utm_url(content="ig_bio_main")),
        ("Reel #1 (Gym Workout Demo)", build_utm_url(content="reel_01_gym_hook")),
        ("Reel #2 (Dance / TikTok Demo)", build_utm_url(content="reel_02_dance_tracking")),
        ("Reel #3 (Solo Traveler POV)", build_utm_url(content="reel_03_travel_solo")),
        ("WhatsApp Status Promo", build_utm_url(source="whatsapp", medium="status", content="wa_status_flash_sale"))
    ]

    for label, url in links:
        print(f"\n{label}:")
        print(f"-> {url}")
    print("=" * 60)
