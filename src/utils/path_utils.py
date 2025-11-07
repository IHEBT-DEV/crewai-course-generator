from pathlib import Path

def resolve_path(relative_path: str) -> Path:
    """
    Resolve a relative path (like 'src/agents/...') to an absolute one
    based on the project root (2 levels above this file).
    """
    project_root = Path(__file__).resolve().parents[2]
    full_path = (project_root / relative_path).resolve()
    return full_path
