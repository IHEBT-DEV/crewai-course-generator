
import re
import logging

logger = logging.getLogger(__name__)

def map_learning_profile_to_strategy(user_input: str) -> str:
    """
    Determine the course strategy based on the learner's profile.

    Expected user_input format: "level, style, goal"
    Example: "2, A, job" or "3, B"

    Mapping guidelines:
      - Experience 1 or 2 + Style A → practical_strategy
      - Experience 1 or 2 + Style B → comprehensive_strategy
      - Experience 1 or 2 + Style C → comprehensive_strategy
      - Experience 3 + Style A → practical_strategy
      - Experience 3 + Style B → academic_strategy
      - Experience 3 + Style C → comprehensive_strategy
      - Experience 4 + Style A → comprehensive_strategy
      - Experience 4 + Style B → academic_strategy
      - Experience 4 + Style C → comprehensive_strategy
    """

    if not user_input:
        logger.warning("No user input provided — defaulting to 'comprehensive_strategy'.")
        return "comprehensive_strategy"

    # Normalize input
    text = user_input.strip().upper()
    parts = [p.strip() for p in re.split(r"[,; ]+", text) if p.strip()]

    # Extract level and style
    level = next((int(p) for p in parts if p.isdigit() and p in {"1", "2", "3", "4"}), None)
    style = next((p for p in parts if p in {"A", "B", "C"}), None)

    # Defaults
    if not level:
        level = 2
        logger.info("No level detected — defaulting to 2 (Some Experience).")
    if not style:
        style = "C"
        logger.info("No style detected — defaulting to 'C' (Comprehensive).")

    # Mapping logic
    mapping_explanation = f"Level={level}, Style={style} → "

    if level in [1, 2]:
        if style == "A":
            strategy = "practical_strategy"
        else:
            strategy = "comprehensive_strategy"
    elif level == 3:
        if style == "A":
            strategy = "practical_strategy"
        elif style == "B":
            strategy = "academic_strategy"
        else:
            strategy = "comprehensive_strategy"
    elif level == 4:
        if style == "A":
            strategy = "comprehensive_strategy"
        elif style == "B":
            strategy = "academic_strategy"
        else:
            strategy = "comprehensive_strategy"
    else:
        strategy = "comprehensive_strategy"

    logger.info(f"{mapping_explanation}{strategy}")
    return strategy
