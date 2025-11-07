import os
import yaml
from crewai import LLM
from dotenv import load_dotenv
import logging
from src.utils.path_utils import resolve_path
from src.utils.logging_utils import log_info, log_ok, log_warning, log_error

load_dotenv()
logger = logging.getLogger(__name__)




class ModelProvider:
    """
    A resilient model manager supporting multiple LLM providers with fallback.
    """

    def __init__(self, provider_name: str = None, model_name: str = None, config_path: str = "src/providers/model_provider.yaml"):
        self.config_path = resolve_path(config_path)
        self.config = self._load_config()
        self.providers = self.config.get("providers", {})
        self.fallback_chain = self.config.get("fallback_chain", [])
        self.provider_name = provider_name.lower() if provider_name else None
        self.model_name = model_name
        self.active_provider = None

    def _load_config(self):
        try:
            with open(self.config_path, "r") as f:
                return yaml.safe_load(f)
        except Exception as e:
            log_error(f"Error loading model_provider.yaml: {e}")
            raise RuntimeError("Unable to load model_provider.yaml")

    def _build_llm(self, provider_name, model_name=None):
        provider_config = self.providers.get(provider_name)
        if not provider_config:
            raise ValueError(f"Unsupported provider: {provider_name}")

        api_env = provider_config.get("api_env")
        api_key = os.getenv(api_env)
        if not api_key:
            raise EnvironmentError(f"Missing environment variable: {api_env}")

        prefix = provider_config.get("prefix", "")
        base_url = provider_config.get("base_url")
        temperature = float(provider_config.get("temperature", 0.7))
        model_name = model_name or provider_config.get("default_model")

        llm_args = {
            "model": f"{prefix}{model_name}",
            "api_key": api_key,
            "temperature": temperature,
        }
        if base_url:
            llm_args["base_url"] = base_url

        logger.debug(f"Building LLM for provider={provider_name}, model={model_name}")
        return LLM(**llm_args)

    def get_llm(self):
        """
        Attempts to create an LLM instance, trying fallbacks if necessary.
        """
        providers_to_try = [self.provider_name] if self.provider_name else self.fallback_chain

        try:
            for provider in providers_to_try:
                try:
                    log_info(f"Attempting LLM creation with provider: {provider}")
                    llm = self._build_llm(provider, self.model_name)
                    self.active_provider = provider
                    log_ok(f" LLM initialized successfully with provider: {provider}")
                    return llm
                except Exception as e:
                    log_warning(f" Provider {provider} failed: {e}. Trying next...")
        except Exception as e:
            # If all providers fail
            log_error(" All LLM providers failed to initialize. Check API keys or connectivity.")
            raise RuntimeError("All LLM provider initializations failed.")
