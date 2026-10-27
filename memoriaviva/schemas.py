"""Pydantic v2 schemas for MemoriaViva (Gemma 4 + Google ADK)."""

from typing import List
from pydantic import BaseModel, Field


class RawFamilyMemory(BaseModel):
    memory_id: str = Field(..., description="Unique identifier for the family memory")
    elder_name: str = Field(..., description="Name and title of the family elder")
    year_recorded: int = Field(..., description="Approximate year or era of the memory")
    cultural_tradition: str = Field(..., description="Cultural heritage or celebration context")
    raw_voice_transcript: str = Field(..., description="Unstructured voice transcript or handwritten card text")
    poetic_measurements: List[str] = Field(..., description="Ancestral measurements like 'a handful of flour'")


class StandardizedIngredient(BaseModel):
    original_phrase: str = Field(..., description="Original ancestral phrase from the elder")
    ingredient_name: str = Field(..., description="Clean culinary ingredient name")
    metric_grams_or_ml: float = Field(..., description="Deterministic metric conversion in grams or milliliters")
    unit: str = Field(..., description="g or ml")
    culinary_note: str = Field(..., description="Texture or temperature cue preserved from the elder")


class WovenHeirloomStoryCard(BaseModel):
    memory_id: str
    title: str
    elder_name: str
    year_recorded: int
    cultural_tradition: str
    verbatim_elder_quote: str
    woven_narrative: str
    standardized_recipe: List[StandardizedIngredient]
    hydration_ratio_pct: float
    air_gapped_verified: bool
    sentry_trace_id: str
    agent_latency_ms: float
