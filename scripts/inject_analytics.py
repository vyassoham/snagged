import os
import glob

analytics_code = """
  <!-- ════════════════════════════════════════════════════
       ANALYTICS & TRACKING ENGINE (Phase 11)
       ════════════════════════════════════════════════════ -->
  <!-- Meta Pixel Code -->
  <script>
  !function(f,b,e,v,n,t,s)
  {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)}(window, document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', 'PIXEL_ID_HERE'); // TODO: Replace with your Meta Pixel ID
  fbq('track', 'PageView');
  </script>
  <noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=PIXEL_ID_HERE&ev=PageView&noscript=1"/></noscript>

  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-XXXXXXXXXX'); // TODO: Replace with your GA4 ID
  </script>
"""

def inject():
    html_files = glob.glob("d:/DropShipping/website/*.html")
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Only inject if not already present
        if "ANALYTICS & TRACKING ENGINE" not in content:
            # Inject right before </head>
            content = content.replace("</head>", f"{analytics_code}</head>")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Injected Analytics into {os.path.basename(file_path)}")
        else:
            print(f"⚡ Analytics already in {os.path.basename(file_path)}")

if __name__ == "__main__":
    inject()
