import os
import glob
import re

GEO_TAGS = """  <!-- GEO-Location & India Market Targeting -->
  <meta name="geo.region" content="IN" />
  <meta name="geo.placename" content="India" />
  <meta name="geo.position" content="20.5937;78.9629" />
  <meta name="ICBM" content="20.5937, 78.9629" />
  <meta name="language" content="en-IN, hi" />
  <meta name="coverage" content="India" />
  <meta name="distribution" content="Global" />
  <meta name="target" content="all" />
"""

INDEX_JSON_LD = """  <!-- Structured Data: Organization & Catalog -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Organization",
        "@id": "https://getsnagged.vercel.app/#organization",
        "name": "Snagged",
        "url": "https://getsnagged.vercel.app/",
        "logo": "https://getsnagged.vercel.app/favicon-32x32.png",
        "description": "Indian DTC creator hardware lab making AI tracking mounts, studio accessories, and audio gear.",
        "telephone": "+91-9210023153",
        "contactPoint": {
          "@type": "ContactPoint",
          "telephone": "+91-9210023153",
          "contactType": "Customer Support",
          "areaServed": "IN",
          "availableLanguage": ["English", "Hindi"]
        }
      },
      {
        "@type": "WebSite",
        "@id": "https://getsnagged.vercel.app/#website",
        "url": "https://getsnagged.vercel.app/",
        "name": "Snagged",
        "publisher": { "@id": "https://getsnagged.vercel.app/#organization" }
      },
      {
        "@type": "ItemList",
        "itemListElement": [
          {
            "@type": "ListItem",
            "position": 1,
            "name": "Snagged 360 AI Auto-Tracker",
            "url": "https://getsnagged.vercel.app/product-ai-tracker.html"
          },
          {
            "@type": "ListItem",
            "position": 2,
            "name": "Snagged M1 Dual Acoustic System",
            "url": "https://getsnagged.vercel.app/product-acoustic-system.html"
          },
          {
            "@type": "ListItem",
            "position": 3,
            "name": "Snagged L1 Magnetic Lumen Block",
            "url": "https://getsnagged.vercel.app/product-lumen-block.html"
          },
          {
            "@type": "ListItem",
            "position": 4,
            "name": "Snagged R1 Articulating Desk Arm",
            "url": "https://getsnagged.vercel.app/product-desk-rig.html"
          }
        ]
      }
    ]
  }
  </script>
"""

PRODUCT_SCHEMAS = {
    "product-ai-tracker.html": """  <!-- Structured Data: Product & FAQ -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org/",
    "@type": "Product",
    "name": "Snagged 360 AI Auto-Tracking Gimbal",
    "image": "https://getsnagged.vercel.app/assets/prod_ai_tracker.jpg",
    "description": "Autonomous 360° optical tracking phone mount for solo content creators. No companion apps or Bluetooth needed.",
    "brand": { "@type": "Brand", "name": "Snagged" },
    "sku": "SNG-AI-360",
    "offers": {
      "@type": "Offer",
      "url": "https://getsnagged.vercel.app/product-ai-tracker.html",
      "priceCurrency": "INR",
      "price": "1399",
      "priceValidUntil": "2027-12-31",
      "availability": "https://schema.org/InStock",
      "itemCondition": "https://schema.org/NewCondition",
      "seller": { "@type": "Organization", "name": "Snagged" }
    }
  }
  </script>
""",
    "product-acoustic-system.html": """  <!-- Structured Data: Product -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org/",
    "@type": "Product",
    "name": "Snagged M1 Dual Acoustic System",
    "image": "https://getsnagged.vercel.app/assets/prod_wireless_mic.jpg",
    "description": "Plug-and-play wireless lavalier microphones with 20m digital frequency transmission for smartphones.",
    "brand": { "@type": "Brand", "name": "Snagged" },
    "sku": "SNG-M1-MIC",
    "offers": {
      "@type": "Offer",
      "url": "https://getsnagged.vercel.app/product-acoustic-system.html",
      "priceCurrency": "INR",
      "price": "999",
      "priceValidUntil": "2027-12-31",
      "availability": "https://schema.org/InStock",
      "itemCondition": "https://schema.org/NewCondition",
      "seller": { "@type": "Organization", "name": "Snagged" }
    }
  }
  </script>
""",
    "product-lumen-block.html": """  <!-- Structured Data: Product -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org/",
    "@type": "Product",
    "name": "Snagged L1 Magnetic Lumen Block",
    "image": "https://getsnagged.vercel.app/assets/prod_lumen_block.jpg",
    "description": "Pocket-sized bi-color LED video light with magnetic backing for solo mobile creators.",
    "brand": { "@type": "Brand", "name": "Snagged" },
    "sku": "SNG-L1-LIGHT",
    "offers": {
      "@type": "Offer",
      "url": "https://getsnagged.vercel.app/product-lumen-block.html",
      "priceCurrency": "INR",
      "price": "699",
      "priceValidUntil": "2027-12-31",
      "availability": "https://schema.org/InStock",
      "itemCondition": "https://schema.org/NewCondition",
      "seller": { "@type": "Organization", "name": "Snagged" }
    }
  }
  </script>
""",
    "product-desk-rig.html": """  <!-- Structured Data: Product -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org/",
    "@type": "Product",
    "name": "Snagged R1 Articulating Desk Arm",
    "image": "https://getsnagged.vercel.app/assets/prod_desk_arm.jpg",
    "description": "Heavy-duty steel articulating scissor arm stand for overhead top-down creator recording.",
    "brand": { "@type": "Brand", "name": "Snagged" },
    "sku": "SNG-R1-RIG",
    "offers": {
      "@type": "Offer",
      "url": "https://getsnagged.vercel.app/product-desk-rig.html",
      "priceCurrency": "INR",
      "price": "1099",
      "priceValidUntil": "2027-12-31",
      "availability": "https://schema.org/InStock",
      "itemCondition": "https://schema.org/NewCondition",
      "seller": { "@type": "Organization", "name": "Snagged" }
    }
  }
  </script>
"""
}

def process_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine canonical URL
    if filename == "index.html":
        canonical_url = "https://getsnagged.vercel.app/"
    else:
        canonical_url = f"https://getsnagged.vercel.app/{filename}"

    canonical_tag = f'  <link rel="canonical" href="{canonical_url}" />\n'

    # Remove previous canonical/geo if any
    content = re.sub(r'  <link rel="canonical".*?\n', '', content)
    content = re.sub(r'  <!-- GEO-Location.*?<meta name="target" content="all" />\n', '', content, flags=re.DOTALL)
    content = re.sub(r'  <!-- Structured Data.*?<\/script>\n', '', content, flags=re.DOTALL)

    # Prepare injected block
    injected_block = canonical_tag + GEO_TAGS

    if filename == "index.html":
        injected_block += INDEX_JSON_LD
    elif filename in PRODUCT_SCHEMAS:
        injected_block += PRODUCT_SCHEMAS[filename]

    # Insert right before </head>
    if "</head>" in content:
        content = content.replace("</head>", f"{injected_block}</head>")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Injected SEO & GEO in: {filepath}")

for path in glob.glob("*.html") + glob.glob("website/*.html"):
    process_file(path)

print("SEO & GEO injection finished successfully!")
