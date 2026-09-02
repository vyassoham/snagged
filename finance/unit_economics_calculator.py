import sys

# Ensure UTF-8 output on Windows terminal
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def calculate_economics(
    selling_price=1999,
    cogs_and_shipping=1150,
    rto_rate_pct=30.0,
    rto_reverse_penalty=60.0,
    cac=0.0,  # 0 for organic
    shopify_fixed_monthly=20.0,
    orders_per_month=100
):
    delivered_rate = (100.0 - rto_rate_pct) / 100.0
    rto_rate = rto_rate_pct / 100.0

    delivered_orders = int(orders_per_month * delivered_rate)
    rto_orders = orders_per_month - delivered_orders

    # Revenue comes only from delivered COD orders
    gross_revenue = delivered_orders * selling_price
    cogs_total = delivered_orders * cogs_and_shipping
    rto_penalty_total = rto_orders * rto_reverse_penalty
    ad_spend_total = orders_per_month * cac

    net_contribution = gross_revenue - cogs_total - rto_penalty_total - ad_spend_total
    net_profit = net_contribution - shopify_fixed_monthly

    gross_margin_per_delivered = selling_price - cogs_and_shipping
    blended_profit_per_order_booked = net_profit / orders_per_month if orders_per_month > 0 else 0

    return {
        "orders_booked": orders_per_month,
        "delivered_orders": delivered_orders,
        "rto_orders": rto_orders,
        "gross_revenue": gross_revenue,
        "cogs_total": cogs_total,
        "rto_penalty_total": rto_penalty_total,
        "ad_spend_total": ad_spend_total,
        "net_profit": net_profit,
        "margin_per_delivered_unit": gross_margin_per_delivered,
        "blended_profit_per_order": round(blended_profit_per_order_booked, 2),
        "breakeven_cac": round(gross_margin_per_delivered * delivered_rate - (rto_rate * rto_reverse_penalty), 2)
    }

def print_dashboard(data):
    print("=" * 65)
    print("         SNAGGED™ FINANCIAL & UNIT ECONOMICS MODEL")
    print("=" * 65)
    print(f"Total Orders Booked          : {data['orders_booked']} orders/month")
    print(f"Delivered Orders (70%)       : {data['delivered_orders']}")
    print(f"RTO / Failed Orders (30%)    : {data['rto_orders']}")
    print("-" * 65)
    print(f"Total Cash Collected         : ₹{data['gross_revenue']:,}")
    print(f"Supplier Cost (COGS + Ship)  : -₹{data['cogs_total']:,}")
    print(f"Courier RTO Penalties        : -₹{data['rto_penalty_total']:,}")
    print(f"Marketing / Ad Spend         : ₹{data['ad_spend_total']:,} (100% Organic)")
    print("-" * 65)
    print(f"NET PROFIT (In Your Pocket)  : ₹{data['net_profit']:,}")
    print(f"Blended Profit Per Order     : ₹{data['blended_profit_per_order']}")
    print(f"Max Breakeven CAC (If ads)   : ₹{data['breakeven_cac']}")
    print("=" * 65)

if __name__ == "__main__":
    model = calculate_economics()
    print_dashboard(model)
