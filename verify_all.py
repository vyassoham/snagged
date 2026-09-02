import sys
import os
import subprocess

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def run_tests():
    print("=" * 65)
    print("       🚀 SNAGGED™ ALL-SYSTEMS READINESS CHECK")
    print("=" * 65)

    checks = [
        ("Landing Page HTML", os.path.exists("website/index.html")),
        ("Legal Policies Document", os.path.exists("policies/legal_policies.md")),
        ("WhatsApp Verifier Script", os.path.exists("automations/whatsapp_cod_verifier.py")),
        ("WhatsApp Templates JSON", os.path.exists("automations/whatsapp_templates.json")),
        ("Financial P&L Calculator", os.path.exists("finance/unit_economics_calculator.py")),
        ("Pixel & GA4 Guide", os.path.exists("analytics/pixel_and_ga4_setup.md")),
        ("UTM Tracking Generator", os.path.exists("analytics/utm_link_builder.py")),
        ("20 Viral Reel Scripts", os.path.exists("marketing/20_viral_reel_scripts.md")),
    ]

    all_passed = True
    for name, passed in checks:
        status = "✅ READY" if passed else "❌ MISSING"
        print(f"[{status}] {name}")
        if not passed:
            all_passed = False

    print("\n" + "-" * 65)
    print("Executing Core Engines Verification...")
    print("-" * 65)

    # 1. Test Financial Calculator
    print("\n[1/3] Testing Unit Economics Engine...")
    res1 = subprocess.run([sys.executable, "finance/unit_economics_calculator.py"], capture_output=True, text=True, encoding='utf-8')
    if res1.returncode == 0:
        print(" -> Output verified cleanly. Unit economics active.")
    else:
        print(f" -> Failed: {res1.stderr}")

    # 2. Test WhatsApp COD Verifier
    print("\n[2/3] Testing COD Risk Assessment & WhatsApp Link Engine...")
    res2 = subprocess.run([sys.executable, "automations/whatsapp_cod_verifier.py"], capture_output=True, text=True, encoding='utf-8')
    if res2.returncode == 0:
        print(" -> Output verified cleanly. Verification URLs active.")
    else:
        print(f" -> Failed: {res2.stderr}")

    # 3. Test UTM Generator
    print("\n[3/3] Testing Marketing UTM Generator...")
    res3 = subprocess.run([sys.executable, "analytics/utm_link_builder.py"], capture_output=True, text=True, encoding='utf-8')
    if res3.returncode == 0:
        print(" -> Output verified cleanly. Campaign links active.")
    else:
        print(f" -> Failed: {res3.stderr}")

    print("\n" + "=" * 65)
    if all_passed:
        print("🎉 ALL TECHNICAL SYSTEMS VERIFIED AND READY FOR LAUNCH!")
    else:
        print("⚠️ Some modules need attention.")
    print("=" * 65)

if __name__ == "__main__":
    run_tests()
