import glob
import re

standard_footer_links = '''<div class="flex items-center gap-6 font-mono text-[10px] tracking-[0.15em] uppercase text-ink-500">
        <a href="https://wa.me/919210023153" target="_blank" class="hover:text-ink-950 transition-colors">WhatsApp</a>
        <a href="shipping.html" class="hover:text-ink-950 transition-colors">Shipping</a>
        <a href="returns.html" class="hover:text-ink-950 transition-colors">Returns</a>
        <a href="privacy.html" class="hover:text-ink-950 transition-colors">Privacy</a>
      </div>'''

# Target any footer nav block with WhatsApp, Shipping, Returns, Privacy
footer_regex = re.compile(
    r'<div class="flex items-center gap-6 font-mono text-\[10px\] tracking-\[0\.15em\] uppercase text-ink-500">.*?</div>',
    re.DOTALL
)

for file in glob.glob("*.html") + glob.glob("website/*.html"):
    if file in ["shipping.html", "returns.html", "privacy.html", "website/shipping.html", "website/returns.html", "website/privacy.html"]:
        continue
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if footer_regex.search(content):
        updated = footer_regex.sub(standard_footer_links, content)
        with open(file, "w", encoding="utf-8") as f:
            f.write(updated)
        print("Updated footer links in:", file)
    else:
        # Also check if footer exists with <footer ...>
        simple_footer = re.compile(r'<footer class="border-t border-canvas-200 py-10">.*?</footer>', re.DOTALL)
        full_footer = f'''<footer class="border-t border-canvas-200 py-10">
    <div class="max-w-[1400px] mx-auto px-5 sm:px-8 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div class="flex items-center gap-4">
        <a href="index.html" class="font-serif italic text-lg text-ink-950">Snagged<span class="text-ember">.</span></a>
        <span class="font-mono text-[10px] tracking-[0.1em] uppercase text-ink-400">© 2026</span>
      </div>
      {standard_footer_links}
    </div>
  </footer>'''
        if simple_footer.search(content):
            updated = simple_footer.sub(full_footer, content)
            with open(file, "w", encoding="utf-8") as f:
                f.write(updated)
            print("Replaced simple footer in:", file)
