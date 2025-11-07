from fastapi import APIRouter, HTTPException
from src.api.schemas.course_request import CourseRequest, CourseResponse
from src.crew import run_course_generation
from src.utils.logging_utils import log_info, log_ok, log_error
from pathlib import Path

router = APIRouter(prefix="/crewai", tags=["CrewAI"])

@router.get("/health")
def health_check():
    """Simple health check endpoint."""
    return {"status": "ok", "message": "CrewAI API is running"}

@router.post("/generate", response_model=CourseResponse)
def generate_course(request: CourseRequest):
    """
    Generate a course using the adaptive CrewAI system.
    """
    try:
        log_info(f"Received course generation request: {request.topic}")
        result = run_course_generation(topic=request.topic, user_input=request.user_input)

        output_dir = Path("outputs")
        latest_file = max(output_dir.glob("*.txt"), key=lambda p: p.stat().st_mtime)

        log_ok(f"Successfully generated course for topic: {request.topic}")
        return CourseResponse(
            strategy=str(result),
            message=f"Course generation completed for topic '{request.topic}'.",
            output_path=str(latest_file)
        )
    except Exception as e:
        log_error(f"Course generation failed: {e}")
        raise HTTPException(status_code=500, detail=f"Generation failed: {e}")
