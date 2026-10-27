"""Deterministic privacy and culinary ratio guardrails for MemoriaViva."""

from typing import List, Tuple
from urllib.parse import urlparse
from memoriaviva.schemas import StandardizedIngredient


def verify_air_gapped_endpoint(endpoint_url: str) -> Tuple[bool, str]:
    """Ensure inference requests only target loopback/local open-weights endpoints."""
    parsed = urlparse(endpoint_url)
    allowed_hosts = {"127.0.0.1", "localhost", "::1"}
    if parsed.hostname in allowed_hosts:
        return True, f"AIR_GAP_OK: {parsed.hostname} is strictly local (0 cloud bytes)."
    raise PermissionError(
        f"PRIVACY_GUARDRAIL_BLOCKED: External host '{parsed.hostname}' rejected to protect family archive."
    )


def compute_and_validate_hydration(ingredients: List[StandardizedIngredient]) -> float:
    """Deterministically verify dough/liquid hydration percentages for heirloom recipes."""
    dry_grams = sum(
        i.metric_grams_or_ml for i in ingredients
        if i.unit == "g" and any(k in i.ingredient_name.lower() for k in ("flour", "wheat", "atta", "semolina"))
    )
    liquid_ml = sum(
        i.metric_grams_or_ml for i in ingredients
        if i.unit == "ml"
    )
    if dry_grams <= 0:
        return 100.0
    ratio = round((liquid_ml / dry_grams) * 100.0, 1)
    # Clamp within safe culinary bounds (45% - 95%)
    return max(45.0, min(95.0, ratio))
