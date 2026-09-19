import os
import glob

PHONE_NUMBER = "919210023153"

files = glob.glob("*.html") + glob.glob("website/*.html")

for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    updated = content.replace("91XXXXXXXXXX", PHONE_NUMBER)
    
    if updated != content:
        with open(f, "w", encoding="utf-8") as file:
            file.write(updated)
        print(f"Updated WhatsApp number in: {f}")
    else:
        print(f"No placeholder found in: {f}")
