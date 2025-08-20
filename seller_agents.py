# seller_agents.py
from typing import Tuple
from environment import Product

class BaseSellerAgent:
    """Interface for hidden sellers used in tests."""
    def _init_(self, min_price: int, personality: str = "standard"):
        self.min_price = int(min_price)
        self.personality = personality

    def get_opening_price(self, product: Product) -> Tuple[int, str]:
        raise NotImplementedError

    def respond_to_buyer(self, buyer_offer: int, round_num: int) -> Tuple[int, str, bool]:
        raise NotImplementedError


class StandardSeller(BaseSellerAgent):
    """Matches the behavior in your template's MockSellerAgent."""
    def get_opening_price(self, product: Product) -> Tuple[int, str]:
        price = int(product.base_market_price * 1.5)
        return price, f"These are premium {product.quality_grade} grade {product.name}. I'm asking ₹{price}."

    def respond_to_buyer(self, buyer_offer: int, round_num: int) -> Tuple[int, str, bool]:
        if buyer_offer >= self.min_price * 1.1:
            return buyer_offer, f"You have a deal at ₹{buyer_offer}!", True
        if round_num >= 8:
            counter = max(self.min_price, int(buyer_offer * 1.05))
            return counter, f"Final offer: ₹{counter}. Take it or leave it.", False
        counter = max(self.min_price, int(buyer_offer * 1.15))
        return counter, f"I can come down to ₹{counter}.", False


class ToughSeller(BaseSellerAgent):
    """Opens higher, concedes slower."""
    def get_opening_price(self, product: Product) -> Tuple[int, str]:
        price = int(product.base_market_price * 1.7)
        return price, f"Top-tier {product.quality_grade} {product.name}. Opening at ₹{price}."

    def respond_to_buyer(self, buyer_offer: int, round_num: int) -> Tuple[int, str, bool]:
        # Requires 12% margin over min_price to accept
        if buyer_offer >= int(self.min_price * 1.12):
            return buyer_offer, f"Fine. Deal at ₹{buyer_offer}.", True
        # Slower concessions; slight leniency near end
        step = 1.12 if round_num < 7 else 1.06
        counter = max(self.min_price, int(buyer_offer * step))
        msg = "Not close. ₹{p}.".format(p=counter) if round_num < 7 else "Last stretch: ₹{p}.".format(p=counter)
        return counter, msg, False


class FriendlySeller(BaseSellerAgent):
    """More cooperative: lower opening and faster convergence."""
    def get_opening_price(self, product: Product) -> Tuple[int, str]:
        price = int(product.base_market_price * 1.35)
        return price, f"Fair price for good {product.quality_grade} {product.name}: ₹{price} to start."

    def respond_to_buyer(self, buyer_offer: int, round_num: int) -> Tuple[int, str, bool]:
        # Accept at 8% over min
        if buyer_offer >= int(self.min_price * 1.08):
            return buyer_offer, f"Happy to agree at ₹{buyer_offer}!", True
        step = 1.10 if round_num < 6 else 1.04
        counter = max(self.min_price, int(buyer_offer * step))
        return counter, f"I can meet you at ₹{counter}.", False
