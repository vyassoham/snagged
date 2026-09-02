# 🚀 Snagged™ — Dropshipping Business Hub & Tech Stack

This workspace contains the complete production assets, automation scripts, legal policies, marketing engines, and financial models for **Snagged™** (AI Auto-Tracker e-commerce brand).

---

## 📁 Repository Structure

```
d:/DropShipping/
├── website/
│   └── index.html                 # Standalone responsive mobile-first landing page with COD checkout & WhatsApp routing
├── policies/
│   └── legal_policies.md          # Indian Consumer Protection (E-Commerce) Rules 2020 compliant policies
├── automations/
│   ├── whatsapp_cod_verifier.py   # Python engine for address risk scoring & automated WhatsApp confirmation link generation
│   └── whatsapp_templates.json    # 12 pre-written customer support, shipping & RTO prevention templates
├── analytics/
│   ├── pixel_and_ga4_setup.md     # Meta Pixel & GA4 tracking implementation guide
│   └── utm_link_builder.py        # Python script generating trackable campaign links for Reels & Bio
├── finance/
│   └── unit_economics_calculator.py# Interactive P&L, CAC, and RTO impact calculator
└── marketing/
    └── 20_viral_reel_scripts.md   # 20 hook-and-shot viral organic video scripts for the 2 partners
```

---

## 🛠️ How to Run & Use the Tech Assets

### 1. View & Test the Landing Page
Double-click `website/index.html` or open it in any browser (Chrome/Edge/Brave).
* Fully responsive and optimized for mobile devices.
* Includes built-in Cash on Delivery order form that stores test orders in `localStorage` and routes confirmed orders to WhatsApp.

### 2. Verify COD Orders & Check RTO Risk
Run the verifier script:
```powershell
python automations/whatsapp_cod_verifier.py
```
Outputs risk score based on phone validity and address depth, and generates the exact pre-filled WhatsApp confirmation URL.

### 3. Calculate Financial Scenarios & Net Profit
Run the financial model:
```powershell
python finance/unit_economics_calculator.py
```
Calculates exact monthly take-home profit factoring in 30% RTO rate and dropshipping margins.

### 4. Generate Trackable Campaign Links
```powershell
python analytics/utm_link_builder.py
```
Generates distinct UTM tags so you can see which specific Instagram Reel made which sale.
