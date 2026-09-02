# Analytics & Conversion Tracking Setup — Snagged

To scale profitably, you must track every visitor journey from Instagram view to Cash on Delivery placement.

---

## 1. META PIXEL SETUP (FACEBOOK & INSTAGRAM)

Even though we are starting with 100% organic content, having the Meta Pixel installed **from Day 1 is critical** because it "seasons" your Pixel with data about who views your site and buys your product. When you later invest in paid ads, Meta will already know your ideal customer profile.

### Step-by-Step Installation:
1. Go to [Meta Events Manager](https://business.facebook.com/events_manager2).
2. Click **Connect Data Sources** -> Select **Web** -> Name it **Snagged Pixel**.
3. Copy your **Pixel ID** (e.g., `123456789012345`).
4. In Shopify:
   - Go to **Apps** -> Search and install **Facebook & Instagram** official app.
   - Connect your personal or business Facebook page.
   - Select Maximum data sharing (Conversions API).
   - Enter your Pixel ID.

---

## 2. GOOGLE ANALYTICS 4 (GA4)

Tracks traffic sources, user bounce rates, session duration, and device types (Android vs. iPhone).

1. Go to [Google Analytics](https://analytics.google.com).
2. Create Account: **Snagged**, Property: **getsnagged.in**.
3. Choose Platform: **Web**.
4. Copy your **Measurement ID** (`G-XXXXXXXXXX`).
5. In Shopify: Go to **Online Store > Preferences** -> Paste Google tag / use Google app.

---

## 3. CORE E-COMMERCE CONVERSION EVENTS TRACKED:
- `PageView` : When any user lands on the site.
- `ViewContent` : When user views the Snagged AI Tracker.
- `AddToCart` : When user clicks "Order Now".
- `InitiateCheckout` : When user begins entering their address.
- `Purchase` : When user hits "PLACE CASH ON DELIVERY ORDER".
