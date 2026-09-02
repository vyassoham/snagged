import sys
import urllib.parse
import re
import json

# Ensure UTF-8 output on Windows terminal
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def assess_rto_risk(order):
    """
    Evaluates risk score from 0 (Safe) to 100 (High Risk) based on Indian COD metrics:
    - Phone number validation
    - Address length & landmark presence
    - Pincode formatting
    """
    risk_score = 0
    flags = []

    # 1. Phone check
    phone = str(order.get('phone', '')).strip()
    clean_phone = re.sub(r'[^0-9]', '', phone)
    if len(clean_phone) == 10 and clean_phone[0] in '6789':
        pass # Valid Indian mobile
    elif len(clean_phone) == 12 and clean_phone.startswith('91') and clean_phone[2] in '6789':
        clean_phone = clean_phone[2:]
    else:
        risk_score += 40
        flags.append("Invalid or suspicious phone number format")

    # 2. Address detail check (Short addresses lead to 70%+ of Indian courier RTOs)
    address = order.get('address', '').strip()
    words = address.split()
    if len(words) < 4:
        risk_score += 35
        flags.append("Address too short (Missing house/flat/street number)")
    
    # 3. Pincode check
    pincode = str(order.get('pincode', '')).strip()
    if not (len(pincode) == 6 and pincode.isdigit()):
        risk_score += 25
        flags.append("Invalid 6-digit pincode")

    return {
        "score": min(risk_score, 100),
        "clean_phone": clean_phone,
        "risk_level": "LOW" if risk_score < 20 else ("MEDIUM" if risk_score < 50 else "HIGH"),
        "flags": flags
    }

def generate_whatsapp_confirmation_link(order):
    """Generates direct clickable WhatsApp chat link with personalized confirmation copy."""
    risk_info = assess_rto_risk(order)
    phone = risk_info['clean_phone']
    name = order.get('name', 'Valued Customer')
    order_id = order.get('order_id', 'SNG-1001')
    city = order.get('city', '')
    pincode = order.get('pincode', '')
    price = order.get('price', '₹1,999')

    message = (
        f"Hey {name}! 👋 Thank you for choosing Snagged! 🚀\n\n"
        f"We received your Cash on Delivery order ({order_id}) for the Snagged™ 360° AI Auto-Tracker ({price}).\n\n"
        f"📍 Delivery to: {city} ({pincode})\n\n"
        f"To ensure our courier team dispatches your package immediately, please reply with *'CONFIRM'*.\n\n"
        f"_(Note: If unconfirmed within 24 hrs, order will be automatically cancelled to prevent bogus orders)._"
    )

    encoded_msg = urllib.parse.quote(message)
    wa_url = f"https://wa.me/91{phone}?text={encoded_msg}"
    
    return {
        "whatsapp_url": wa_url,
        "risk_assessment": risk_info,
        "formatted_message": message
    }

if __name__ == "__main__":
    sample_order = {
        "order_id": "SNG-948210",
        "name": "Arjun Sharma",
        "phone": "9876543210",
        "address": "Flat 402, Sunshine Heights, Near Metro Station, Sector 21",
        "city": "Gurugram",
        "pincode": "122016",
        "price": "₹1,999"
    }

    result = generate_whatsapp_confirmation_link(sample_order)
    print("=" * 60)
    print("SNAGGED ORDER VERIFICATION & RTO SHIELD")
    print("=" * 60)
    print(f"Order ID   : {sample_order['order_id']}")
    print(f"Customer   : {sample_order['name']} ({sample_order['phone']})")
    print(f"Risk Level : {result['risk_assessment']['risk_level']} (Score: {result['risk_assessment']['score']}/100)")
    if result['risk_assessment']['flags']:
        print(f"Flags      : {', '.join(result['risk_assessment']['flags'])}")
    print("\nGenerated WhatsApp Verification URL:")
    print(result['whatsapp_url'])
    print("=" * 60)
