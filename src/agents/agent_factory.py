from typing import Optional, List
import yaml
from crewai import Agent
from src.providers.model_provider import ModelProvider
from src.utils.path_utils import resolve_path
from src.utils.logging_utils import log_ok, log_agent, log_error, log_warning, log_info

# Tools
from src.tools.arxiv_tool import ArxivTool
from src.tools.scraper_tool import ScraperTool
from src.tools.duckduckgo_tool import DuckDuckGoTool
from src.tools.semantic_scholar_tool import SemanticScholarTool


def create_agent_with_path(path: str) -> Agent:
    return AgentFactory(path).create_agent()


class AgentFactory:
    """Factory to build CrewAI Agents dynamically from YAML configuration."""

    def __init__(self, config_path: str):
        self.config_path = resolve_path(config_path)
        self.config = self._load_config() if config_path else None

    def _load_config(self):
        if not self.config_path.exists():
            raise FileNotFoundError(f"Agent config not found: {self.config_path}")
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f)
            log_ok(f"Loaded agent config: {self.config_path}")
            return config
        except Exception as e:
            log_error(f"Failed to load agent config {self.config_path}: {e}")
            raise

    def _initialize_llm(self):
        llm_cfg = self.config.get("llm", {})
        provider = llm_cfg.get("provider")
        model = llm_cfg.get("model")
        if not provider:
            raise ValueError("No LLM provider specified in agent config.")
        log_info(f"Initializing LLM -> provider={provider}, model={model}")
        return ModelProvider(provider_name=provider, model_name=model).get_llm()

    def _get_tools_for_agent(self) -> Optional[List]:
        """Attach predefined tools for researcher agents."""
        agent_name = self.config_path.stem.lower()
        tools = []
        if "researcher" in agent_name:
            try:
                for tool_cls in [ArxivTool, ScraperTool, DuckDuckGoTool, SemanticScholarTool]:
                    tools.append(tool_cls())
                    log_info(f"Attached {tool_cls.__name__} to {agent_name}")
            except Exception as e:
                log_warning(f"Error attaching tools to {agent_name}: {e}")
        return tools or None

    def create_agent(self) -> Agent:
        agent_cfg = self.config.get("agent", {})
        llm = self._initialize_llm()
        tools = self._get_tools_for_agent()
        agent = Agent(
            role=agent_cfg.get("role", "Generic Agent"),
            goal=agent_cfg.get("goal", "Assist in AI-driven tasks."),
            backstory=agent_cfg.get("backstory", "An AI agent ready to perform tasks."),
            allow_delegation=agent_cfg.get("allow_delegation", False),
            verbose=agent_cfg.get("verbose", False),
            llm=llm,
            tools=tools,
        )
        log_agent(f"Created agent '{agent_cfg.get('role', 'Unnamed')}'")
        return agent
