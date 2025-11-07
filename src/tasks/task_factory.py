import datetime

import yaml
from typing import Optional, List, Dict, Any
from crewai import Task
from src.agents.agent_factory import AgentFactory
from src.utils.path_utils import resolve_path
from src.utils.logging_utils import log_ok, log_task
from src.tasks.output_models import (
    Resources,
    Plan,
    Lesson,
    Workshop,
    Course,
    AlgorithmImplementation,
    PaperAnalysis,
    TheoreticalExercises,
    CodeChallenges,
    HandsOnExercises,
    ProjectBuilding,
    CaseStudy,
    MiniProjects,
    MixedExercises, AcademicFullCourse, PracticalFullCourse, ComprehensiveFullCourse,
)

OUTPUT_MODEL_REGISTRY = {
    "Resources": Resources,
    "Plan": Plan,
    "Lesson": Lesson,
    "Workshop": Workshop,
    "Course": Course,
    "AlgorithmImplementation": AlgorithmImplementation,
    "PaperAnalysis": PaperAnalysis,
    "TheoreticalExercises": TheoreticalExercises,
    "CodeChallenges": CodeChallenges,
    "HandsOnExercises": HandsOnExercises,
    "ProjectBuilding": ProjectBuilding,
    "CaseStudy": CaseStudy,
    "MiniProjects": MiniProjects,
    "MixedExercises": MixedExercises,
    "AcademicFullCourse": AcademicFullCourse,
    "PracticalFullCourse": PracticalFullCourse,
    "ComprehensiveFullCourse": ComprehensiveFullCourse
}



def _load_output_model(name: Optional[str]):
    return OUTPUT_MODEL_REGISTRY.get(name)


def _create_agent(path: str):
    factory = AgentFactory(path)
    return factory.create_agent()


class TaskFactory:
    """Factory to build CrewAI Tasks dynamically from YAML configuration files."""

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = resolve_path(config_path) if config_path else None
        self.config = self._load_config() if config_path else None

    def _load_config(self) -> Dict[str, Any]:
        if not self.config_path.exists():
            raise FileNotFoundError(f"Task config not found: {self.config_path}")
        with open(self.config_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        log_ok(f"Loaded task config: {self.config_path}")
        return data

    def create_task(self, context_tasks: Optional[List[Task]] = None) -> Task:
        cfg = self.config.get("task", {})
        agent_path = cfg.get("agent")
        agent = _create_agent(agent_path)
        task_name = cfg.get("name")
        model = _load_output_model(cfg.get("output_json"))
        output_path =f"outputs/tasks/{task_name}_{datetime.datetime.now():%Y%m%d_%H%M%S}.txt"
        task = Task(
            description=cfg.get("description", ""),
            expected_output=cfg.get("expected_output", ""),
            agent=agent,
            context=context_tasks or [],
            output_json=model,
            output_file=output_path
        )
        log_task(f"Created task from {self.config_path}")
        return task
