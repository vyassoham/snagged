import os
import re
import glob

# 1. Update index.html
def update_index(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Product 1: AI Tracker card
    p1_old = re.compile(
        r'<div class="card-img-main absolute inset-0 flex flex-col items-center justify-center p-8 bg-gradient-to-b from-canvas-100 to-canvas-200">\s*<div class="text-6xl mb-4">🤖</div>\s*<span class="font-mono text-\[10px\] tracking-\[0\.15em\] uppercase text-ink-500">360° AI Tracking</span>\s*</div>\s*<div class="card-img-hover absolute inset-0 flex flex-col items-center justify-center p-8 bg-gradient-to-b from-ink-900 to-ink-950">\s*<div class="text-5xl mb-3">👌</div>\s*<span class="font-mono text-\[10px\] tracking-\[0\.15em\] uppercase text-ink-400">Gesture Control Demo</span>\s*</div>',
        re.DOTALL
    )
    p1_new = '<img src="assets/prod_ai_tracker.jpg" alt="Snagged 360 AI Auto-Tracker" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />'
    content = p1_old.sub(p1_new, content)

    # Product 2: Wireless Mic card
    p2_old = re.compile(
        r'<div class="card-img-main absolute inset-0 flex flex-col items-center justify-center p-8 bg-gradient-to-b from-canvas-100 to-canvas-200">\s*<div class="text-6xl mb-4">🎙️</div>\s*<span class="font-mono text-\[10px\] tracking-\[0\.15em\] uppercase text-ink-500">Dual Acoustic System</span>\s*</div>\s*<div class="card-img-hover absolute inset-0 flex flex-col items-center justify-center p-8 bg-gradient-to-b from-ink-900 to-ink-950">\s*<div class="text-5xl mb-3">⚡</div>\s*<span class="font-mono text-\[10px\] tracking-\[0\.15em\] uppercase text-ink-400">Plug & Play Receiver</span>\s*</div>',
        re.DOTALL
    )
    p2_new = '<img src="assets/prod_wireless_mic.jpg" alt="Snagged M1 Wireless Mics" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />'
    content = p2_old.sub(p2_new, content)

    # Product 3: Magnetic Light card
    p3_old = re.compile(
        r'<div class="card-img-main absolute inset-0 flex flex-col items-center justify-center p-8 bg-gradient-to-b from-canvas-100 to-canvas-200">\s*<div class="text-6xl mb-4">💡</div>\s*<span class="font-mono text-\[10px\] tracking-\[0\.15em\] uppercase text-ink-500">Magnetic Lumen Block</span>\s*</div>\s*<div class="card-img-hover absolute inset-0 flex flex-col items-center justify-center p-8 bg-gradient-to-b from-ink-900 to-ink-950">\s*<div class="text-5xl mb-3">🧲</div>\s*<span class="font-mono text-\[10px\] tracking-\[0\.15em\] uppercase text-ink-400">Mounts to any metal</span>\s*</div>',
        re.DOTALL
    )
    p3_new = '<img src="assets/prod_lumen_block.jpg" alt="Snagged L1 Pocket Light" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />'
    content = p3_old.sub(p3_new, content)

    # Product 4: Desk Rig card
    p4_old = re.compile(
        r'<div class="card-img-main absolute inset-0 flex flex-col items-center justify-center p-8 bg-gradient-to-b from-canvas-100 to-canvas-200">\s*<div class="text-6xl mb-4">🦾</div>\s*<span class="font-mono text-\[10px\] tracking-\[0\.15em\] uppercase text-ink-500">Articulating Desk Rig</span>\s*</div>\s*<div class="card-img-hover absolute inset-0 flex flex-col items-center justify-center p-8 bg-gradient-to-b from-ink-900 to-ink-950">\s*<div class="text-5xl mb-3">🏗️</div>\s*<span class="font-mono text-\[10px\] tracking-\[0\.15em\] uppercase text-ink-400">100% Metal Construction</span>\s*</div>',
        re.DOTALL
    )
    p4_new = '<img src="assets/prod_desk_arm.jpg" alt="Snagged R1 Overhead Arm" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />'
    content = p4_old.sub(p4_new, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated catalog cards in:", filepath)

# 2. Update Product Detail Pages
def update_pdp(filepath, image_filename, alt_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the aspect-square main image container
    pattern = re.compile(
        r'<div class="aspect-square bg-canvas-100 border border-canvas-200 rounded-sm overflow-hidden flex flex-col items-center justify-center relative">.*?</div>\s*</div>',
        re.DOTALL
    )
    new_block = f'''<div class="aspect-square bg-canvas-100 border border-canvas-200 rounded-sm overflow-hidden relative shadow-sm">
            <span class="absolute top-4 left-4 z-10 font-mono text-[9px] tracking-[0.15em] uppercase bg-ink-950/80 backdrop-blur-sm text-canvas-50 px-2.5 py-1 rounded-sm">Official Studio Shot</span>
            <img src="{image_filename}" alt="{alt_text}" class="w-full h-full object-cover" />
          </div>'''
    
    # Simpler targeted replace
    old_simple = re.compile(r'<div class="aspect-square bg-canvas-100 border border-canvas-200 rounded-sm overflow-hidden flex flex-col items-center justify-center relative">.*?</div>', re.DOTALL)
    
    # We replace the first aspect-square main block
    match = old_simple.search(content)
    if match:
        content = content[:match.start()] + f'''<div class="aspect-square bg-canvas-100 border border-canvas-200 rounded-sm overflow-hidden relative shadow-sm">
            <span class="absolute top-4 left-4 z-10 font-mono text-[9px] tracking-[0.15em] uppercase bg-ink-950/80 backdrop-blur-sm text-canvas-50 px-2.5 py-1 rounded-sm">Official Studio Shot</span>
            <img src="{image_filename}" alt="{alt_text}" class="w-full h-full object-cover" />
          </div>''' + content[match.end():]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated PDP hero image in: {filepath}")

# Execute across all matching files
update_index("index.html")
update_index("website/index.html")

update_pdp("product-ai-tracker.html", "assets/prod_ai_tracker.jpg", "Snagged 360 AI Auto-Tracker")
update_pdp("website/product-ai-tracker.html", "assets/prod_ai_tracker.jpg", "Snagged 360 AI Auto-Tracker")

update_pdp("product-acoustic-system.html", "assets/prod_wireless_mic.jpg", "Snagged M1 Dual Acoustic System")
update_pdp("website/product-acoustic-system.html", "assets/prod_wireless_mic.jpg", "Snagged M1 Dual Acoustic System")

update_pdp("product-lumen-block.html", "assets/prod_lumen_block.jpg", "Snagged L1 Magnetic Lumen Block")
update_pdp("website/product-lumen-block.html", "assets/prod_lumen_block.jpg", "Snagged L1 Magnetic Lumen Block")

update_pdp("product-desk-rig.html", "assets/prod_desk_arm.jpg", "Snagged R1 Articulating Desk Arm")
update_pdp("website/product-desk-rig.html", "assets/prod_desk_arm.jpg", "Snagged R1 Articulating Desk Arm")
