import os
from PIL import Image, ImageDraw, ImageFont

def generate_favicon():
    # Supersampling factor for ultra-sharp downsampling
    size = 256
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Brand Colors
    INK = (26, 24, 20, 255)       # #1A1814
    CANVAS = (250, 248, 245, 255) # #FAF8F5
    EMBER = (194, 101, 58, 255)   # #C2653A

    # Rounded background
    corner_radius = 56
    draw.rounded_rectangle(
        [(0, 0), (size - 1, size - 1)],
        radius=corner_radius,
        fill=INK
    )

    # Draw letter 'S'
    font = None
    # Try finding an installed serif font on Windows (Georgia, Times New Roman, etc.)
    font_paths = [
        "C:/Windows/Fonts/georgiai.ttf", # Georgia Italic
        "C:/Windows/Fonts/georgia.ttf",  # Georgia Regular
        "C:/Windows/Fonts/timesi.ttf",   # Times Italic
        "C:/Windows/Fonts/times.ttf",    # Times Regular
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                font = ImageFont.truetype(path, 168)
                break
            except Exception:
                continue

    if font is None:
        font = ImageFont.load_default()

    # Draw 'S'
    bbox = draw.textbbox((0, 0), "S", font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    text_x = (size - text_w) // 2 - 12
    text_y = (size - text_h) // 2 - 20
    draw.text((text_x, text_y), "S", font=font, fill=CANVAS)

    # Draw Ember accent dot
    dot_radius = 22
    dot_cx = size - 54
    dot_cy = 64
    draw.ellipse(
        [
            (dot_cx - dot_radius, dot_cy - dot_radius),
            (dot_cx + dot_radius, dot_cy + dot_radius)
        ],
        fill=EMBER
    )

    # Create sizes: 16x16, 32x32, 48x48
    sizes = [(16, 16), (32, 32), (48, 48)]
    resized_images = [img.resize(s, Image.Resampling.LANCZOS) for s in sizes]

    # Save favicon.ico with multi-resolution support
    output_ico = "d:/DropShipping/website/favicon.ico"
    resized_images[1].save(
        output_ico,
        format="ICO",
        sizes=sizes,
        append_images=[resized_images[0], resized_images[2]]
    )
    print(f"Generated {output_ico}")

    # Also save 32x32 PNG as standard web icon fallback
    output_png = "d:/DropShipping/website/favicon-32x32.png"
    resized_images[1].save(output_png, format="PNG")
    print(f"Generated {output_png}")

if __name__ == "__main__":
    generate_favicon()
