import glob
import re

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Index & Catalog cards updates
    # AI Tracker
    content = content.replace('₹1,999', '₹1,399')
    content = content.replace('1999', '1399')

    # Wireless Mics
    content = content.replace('₹1,499', '₹999')
    content = content.replace('1499', '999')

    # Lumen Block
    content = content.replace('₹1,199', '₹699')
    content = content.replace('1199', '699')

    # Desk Rig
    content = content.replace('₹1,799', '₹1,099')
    content = content.replace('1799', '1099')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated pricing in:", filepath)

# Update all html files in root and website/
for path in glob.glob("*.html") + glob.glob("website/*.html"):
    update_file(path)

print("Mass market pricing successfully applied across all pages!")
