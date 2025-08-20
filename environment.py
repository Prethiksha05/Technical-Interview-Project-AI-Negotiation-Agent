# environment.py
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List
import os
import random

# --------- ENV LOADING (no external deps required) ----------
def load_env():
    # Simple .env loader (only KEY=VALUE lines)
    env_path = ".env"
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())

load_env()

# Global settings (can be overridden by .env)
MAX_ROUNDS = int(os.getenv("MAX_ROUNDS", "10"))
RANDOM_SEED = os.getenv("RANDOM_SEED")
if RANDOM_SEED is not None and RANDOM_SEED != "":
    random.seed(int(RANDOM_SEED))

CURRENCY = os.getenv("CURRENCY", "₹")

# ---------------- Core Data Structures ----------------------
@dataclass
class Product:
    name: str
    category: str
    quantity: int
    quality_grade: str  # 'A', 'B', or 'Export'
    origin: str
    base_market_price: int
    attributes: Dict[str, Any]

@dataclass
class NegotiationContext:
    product: Product
    your_budget: int
    current_round: int
    seller_offers: List[int]
    your_offers: List[int]
    messages: List[Dict[str, str]]

class DealStatus(Enum):
    ONGOING = "ongoing"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    TIMEOUT = "timeout"

# ----------------------- Utilities --------------------------
def money(n: int) -> str:
    return f"{CURRENCY}{n:,}"

def clamp_price(price: int, budget: int) -> int:
    return min(max(0, int(price)), int(budget))

def scenario_triplets(market_price: int) -> Dict[str, Dict[str, int]]:
    return {
        "easy":   {"buyer_budget": int(market_price * 1.2), "seller_min": int(market_price * 0.80)},
        "medium": {"buyer_budget": int(market_price * 1.0), "seller_min": int(market_price * 0.85)},
        "hard":   {"buyer_budget": int(market_price * 0.9), "seller_min": int(market_price * 0.82)},
    }
