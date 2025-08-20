from typing import Dict, Any
from environment import Product, NegotiationContext, DealStatus, money, scenario_triplets, MAX_ROUNDS
from seller_agents import StandardSeller  # You can swap to ToughSeller/FriendlySeller
import importlib
import sys

def load_buyer() -> Any:
    """
    Import YourBuyerAgent from your existing single file.
    Change the module name below if your file has a different name.
    """
    # If your file is named interview_negotiation_template.py, use that:
    module_name = "interview_negotiation_template"
    mod = importlib.import_module(module_name)
    return mod.YourBuyerAgent("StrategicAnalyst")

def run_negotiation_test(buyer_agent, product: Product, buyer_budget: int, seller_min: int) -> Dict[str, Any]:
    seller = StandardSeller(seller_min)
    context = NegotiationContext(
        product=product,
        your_budget=buyer_budget,
        current_round=0,
        seller_offers=[],
        your_offers=[],
        messages=[]
    )
    # Seller opens
    seller_price, seller_msg = seller.get_opening_price(product)
    context.seller_offers.append(seller_price)
    context.messages.append({"role": "seller", "message": seller_msg})

    deal_made = False
    final_price = None

    for round_num in range(MAX_ROUNDS):
        context.current_round = round_num + 1

        if round_num == 0:
            buyer_offer, buyer_msg = buyer_agent.generate_opening_offer(context)
            status = DealStatus.ONGOING
        else:
            status, buyer_offer, buyer_msg = buyer_agent.respond_to_seller_offer(context, seller_price, seller_msg)

        context.your_offers.append(buyer_offer)
        context.messages.append({"role": "buyer", "message": buyer_msg})

        if status == DealStatus.ACCEPTED:
            deal_made = True
            final_price = seller_price
            break

        seller_price, seller_msg, seller_accepts = seller.respond_to_buyer(buyer_offer, round_num)

        if seller_accepts:
            deal_made = True
            final_price = buyer_offer
            context.messages.append({"role": "seller", "message": seller_msg})
            break

        context.seller_offers.append(seller_price)
        context.messages.append({"role": "seller", "message": seller_msg})

    result = {
        "deal_made": deal_made,
        "final_price": final_price,
        "rounds": context.current_round,
        "savings": (buyer_budget - final_price) if deal_made else 0,
        "savings_pct": ((buyer_budget - final_price) / buyer_budget * 100) if deal_made else 0.0,
        "below_market_pct": ((product.base_market_price - final_price) / product.base_market_price * 100) if deal_made else 0.0,
        "conversation": context.messages,
    }
    return result

def test_suite():
    products = [
        Product(
            name="Alphonso Mangoes", category="Mangoes", quantity=100, quality_grade="A",
            origin="Ratnagiri", base_market_price=180000,
            attributes={"ripeness": "optimal", "export_grade": True}
        ),
        Product(
            name="Kesar Mangoes", category="Mangoes", quantity=150, quality_grade="B",
            origin="Gujarat", base_market_price=150000,
            attributes={"ripeness": "semi-ripe", "export_grade": False}
        ),
    ]

    buyer = load_buyer()
    print("=" * 60)
    print(f"TESTING BUYER: {buyer.name}")
    print(f"Personality: {buyer.personality['personality_type']}")
    print("=" * 60)

    total_savings = 0
    deals_made = 0

    for product in products:
        scenarios = scenario_triplets(product.base_market_price)
        for label, cfg in scenarios.items():
            buyer_budget = cfg["buyer_budget"]
            seller_min = cfg["seller_min"]

            print(f"\nTest: {product.name} — {label}")
            print(f"Budget: {money(buyer_budget)} | Market: {money(product.base_market_price)} | Seller min: {money(seller_min)}")

            result = run_negotiation_test(buyer, product, buyer_budget, seller_min)
            if result["deal_made"]:
                deals_made += 1
                total_savings += result["savings"]
                print(f"✅ DEAL at {money(result['final_price'])} in {result['rounds']} rounds")
                print(f"   Savings: {money(result['savings'])} ({result['savings_pct']:.1f}%)")
                print(f"   Below Market: {result['below_market_pct']:.1f}%")
            else:
                print(f"❌ NO DEAL after {result['rounds']} rounds")

    print("\n" + "=" * 60)
    print("SUMMARY")
    print(f"Deals Completed: {deals_made}/6")
    print(f"Total Savings: {money(total_savings)}")
    print("=" * 60)

if _name_ == "_main_":
    # Optional: allow passing the buyer module as CLI arg
    if len(sys.argv) > 1:
        # If you pass an alternative module, override loader
        import importlib
        m = importlib.import_module(sys.argv[1])
        buyer = m.YourBuyerAgent("StrategicAnalyst")
        # quick single run to verify
        test_suite()
    else:
        test_suite()
