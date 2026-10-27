"""Unit tests for MemoriaViva schemas, guardrails, and Google ADK + Gemma 4 pipeline."""

import pytest
from memoriaviva.guardrails import verify_air_gapped_endpoint, compute_and_validate_hydration
from memoriaviva.dashboard import SAMPLE_MEMORIES, pipeline


def test_air_gapped_guardrail_allows_localhost():
    ok, msg = verify_air_gapped_endpoint("http://127.0.0.1:11434")
    assert ok is True
    assert "AIR_GAP_OK" in msg


def test_air_gapped_guardrail_blocks_external_cloud():
    with pytest.raises(PermissionError):
        verify_air_gapped_endpoint("https://api.external-cloud.example.com/v1/chat")


def test_pipeline_weaves_all_sample_memories():
    for raw in SAMPLE_MEMORIES:
        card = pipeline.weave_memory(raw)
        assert card.air_gapped_verified is True
        assert len(card.standardized_recipe) == 3
        assert 45.0 <= card.hydration_ratio_pct <= 100.0
