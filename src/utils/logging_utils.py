import logging

# Configure global logging once
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

logger = logging.getLogger("course_creator")

# --- Semantic Log Helpers ---------------------------------------------------

def log_ok(message: str):
    logger.info(f"[OK] {message}")

def log_info(message: str):
    logger.info(f"[INFO] {message}")

def log_agent(message: str):
    logger.info(f"[AGENT] {message}")

def log_task(message: str):
    logger.info(f"[TASK] {message}")

def log_warning(message: str):
    logger.warning(f"[WARN] {message}")

def log_error(message: str):
    logger.error(f"[ERROR] {message}")
def log_step(message: str):
    logger.info(f"[STEP] {message}")