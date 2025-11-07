import yaml
from pathlib import Path
from typing import Dict, List, Any
from crewai import Crew, Process, Task
from src.agents.agent_factory import AgentFactory
from src.tasks.task_factory import TaskFactory
from src.utils.logging_utils import log_ok, log_task, log_agent
from src.utils.path_utils import resolve_path


class StrategyFactory:
    """Builds a complete Crew (agents + tasks) per strategy."""

    def __init__(self, strategy_config_path: str):
        self.strategy_config_path = resolve_path(strategy_config_path)
        self.config = self._load_strategies()

    def _load_strategies(self) -> Dict[str, Any]:
        with open(self.strategy_config_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        log_ok(f"Loaded strategies config: {self.strategy_config_path}")
        return data

    def create_agents_for_strategy(self, name: str) -> Dict[str, List]:
        cfg = self.config[name]
        agents = {"course_creation": [], "workshops": []}
        for phase in ["course_creation", "workshops"]:
            for agent_path in cfg[phase]["agents"]:
                a = AgentFactory(agent_path).create_agent()
                agents[phase].append(a)
                log_agent(f"Loaded {phase} agent from {agent_path}")
        return agents

    def create_tasks_for_strategy(self, name: str) -> Dict[str, List[Task]]:
        cfg = self.config[name]
        tasks = {"course_creation": [], "workshops": []}
        prev = None
        for t_path in cfg["course_creation"]["tasks"]:
            t = TaskFactory(t_path).create_task([prev] if prev else None)
            tasks["course_creation"].append(t)
            prev = t
            log_task(f"Created course task from {t_path}")
        for t_path in cfg["workshops"]["tasks"]:
            t = TaskFactory(t_path).create_task()
            tasks["workshops"].append(t)
            log_task(f"Created workshop task from {t_path}")
        return tasks

    def build_crew_for_strategy(self, name: str, process_type: str = "sequential") -> Crew:
        agents = self.create_agents_for_strategy(name)
        tasks = self.create_tasks_for_strategy(name)
        all_agents = agents["course_creation"] + agents["workshops"]
        all_tasks = tasks["course_creation"] + tasks["workshops"]

        # Add global integrator agent + task
        integrator_agent_path = "src/agents/integrator_agent.yaml"
        integrator_task_path = "src/tasks/integration_task.yaml"
        integrator_agent = AgentFactory(integrator_agent_path).create_agent()
        integration_task = TaskFactory(integrator_task_path).create_task(context_tasks=all_tasks)

        all_agents.append(integrator_agent)
        all_tasks.append(integration_task)

        process = Process.parallel if process_type == "parallel" else Process.sequential
        crew = Crew(agents=all_agents, tasks=all_tasks, process=process, verbose=True)
        log_ok(f"Crew for {name} ready with {len(all_agents)} agents and {len(all_tasks)} tasks.")
        return crew
