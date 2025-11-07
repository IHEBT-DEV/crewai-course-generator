from datetime import datetime
from pathlib import Path
from crewai import Crew
from src.strategies.strategy_factory import StrategyFactory
from src.agents.agent_factory import AgentFactory
from src.tasks.task_factory import TaskFactory
from src.utils.helpers import map_learning_profile_to_strategy
from src.utils.logging_utils import log_ok, log_warning, log_info
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

CLASSIFIER_AGENT_PATH = "src/agents/classifier_agent.yaml"

def classify_strategy(topic: str,user_input: str = None) -> str:
    try:
        classifier = AgentFactory(CLASSIFIER_AGENT_PATH).create_agent()
        task = TaskFactory("src/tasks/classification_task.yaml").create_task()
        result = Crew(agents=[classifier], tasks=[task]).kickoff(inputs={"topic": topic, "user_input": user_input})
        log_ok(f"Strategy classified: {result}")
        return result.strip().lower()
    except Exception as e:
        log_warning(f"Classification failed ({e}) → defaulting to 'academic_strategy'")
        return "academic_strategy"

def run_course_generation(topic: str,user_input: str = None):
    strategy = map_learning_profile_to_strategy(user_input)
    log_info(f"Starting generation for: {topic} and strategy : {strategy}")
    #strategy = classify_strategy(topic,user_input)
    factory = StrategyFactory("src/strategies/strategies.yaml")
    crew = factory.build_crew_for_strategy(strategy)
    result = crew.kickoff(inputs={"topic": topic})

    Path("outputs").mkdir(exist_ok=True)
    output_path = Path("outputs") / f"{strategy}_{datetime.now():%Y%m%d_%H%M%S}.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(result))
    log_ok(f"Course generation complete. Output: {output_path}")
    return result

if __name__ == "__main__":
    inputs={"topic":'machine learning','user_inputs':'2,A'}
    output = run_course_generation(topic=inputs['topic'],user_input=inputs['user_inputs'])
    print("\n=== FINAL COURSE OUTPUT ===\n")
    print(output)
