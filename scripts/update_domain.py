import glob

for f in glob.glob("*.html") + glob.glob("website/*.html"):
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    updated = content.replace("https://snagged-store.vercel.app/", "https://getsnagged.vercel.app/")
    if updated != content:
        with open(f, "w", encoding="utf-8") as file:
            file.write(updated)
        print("Updated domain in:", f)
