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

