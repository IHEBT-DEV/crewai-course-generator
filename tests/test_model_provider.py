import os
import pytest
from unittest.mock import patch, MagicMock
from src.providers.model_provider import ModelProvider

# -------------------------------------------------------------------------
# FIXTURES
# -------------------------------------------------------------------------

@pytest.fixture(scope="module")
def config_path():
    return "src/providers/model_provider.yaml"

@pytest.fixture(autouse=True)
def setup_env(monkeypatch):
    """Sets up fake API keys for testing."""
    monkeypatch.setenv("GOOGLE_API_KEY", "fake-google-key")
    monkeypatch.setenv("OPENROUTER_API_KEY", "fake-openrouter-key")
    monkeypatch.setenv("MISTRAL_API_KEY", "fake-mistral-key")
    monkeypatch.setenv("HF_TOKEN", "fake-hf-key")

# -------------------------------------------------------------------------
# TESTS
# -------------------------------------------------------------------------

def test_load_config(config_path):
    """Ensure YAML config loads correctly."""
    provider = ModelProvider(config_path=config_path)
    assert "providers" in provider.config
    assert "google" in provider.providers
    assert "fallback_chain" in provider.config


@patch("src.providers.model_provider.LLM", autospec=True)
def test_successful_llm_creation(mock_llm, config_path):
    """Test successful LLM creation with valid provider."""
    provider = ModelProvider(provider_name="google", config_path=config_path)
    llm_instance = provider.get_llm()
    mock_llm.assert_called_once()
    assert provider.active_provider == "google"
    assert llm_instance is not None


@patch("src.providers.model_provider.LLM", side_effect=Exception("Fake Failure"))
def test_fallback_logic(mock_llm, config_path):
    """Test automatic fallback when first provider fails."""
    provider = ModelProvider(provider_name=None, config_path=config_path)
    # Should try multiple providers due to failure
    with pytest.raises(RuntimeError):
        provider.get_llm()

    # Verify multiple attempts
    assert mock_llm.call_count > 1


@patch("src.providers.model_provider.LLM", autospec=True)
def test_missing_api_key(monkeypatch, mock_llm, config_path):
    """Test that missing API key raises an error."""
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    provider = ModelProvider(provider_name="google", config_path=config_path)
    with pytest.raises(EnvironmentError):
        provider.get_llm()


@patch("src.providers.model_provider.LLM", side_effect=Exception("All Fail"))
def test_all_providers_fail(mock_llm, config_path):
    """Ensure a RuntimeError is raised when all providers fail."""
    provider = ModelProvider(config_path=config_path)
    with pytest.raises(RuntimeError, match="All LLM provider initializations failed"):
        provider.get_llm()
