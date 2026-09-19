import os
import glob
import argparse

def update_credentials(phone, pixel, ga4):
    html_files = glob.glob("d:/DropShipping/website/*.html")
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace WhatsApp Number
        if phone:
            content = content.replace("91XXXXXXXXXX", f"91{phone}")
            
        # Replace Pixel ID
        if pixel:
            content = content.replace("PIXEL_ID_HERE", pixel)
            
        # Replace GA4 ID
        if ga4:
            content = content.replace("G-XXXXXXXXXX", ga4)
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print("✅ Successfully updated all credentials across the website!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--phone", help="10-digit WhatsApp Number")
    parser.add_argument("--pixel", help="Meta Pixel ID")
    parser.add_argument("--ga4", help="GA4 Measurement ID")
    args = parser.parse_args()
    
    update_credentials(args.phone, args.pixel, args.ga4)
