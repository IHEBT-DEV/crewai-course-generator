from pydantic import BaseModel, Field
from typing import Optional

class CourseRequest(BaseModel):
    topic: str = Field(..., description="Course topic, e.g. 'Machine Learning' or 'Docker'")
    user_input: Optional[str] = Field(
        None,
        description="User learning profile (e.g., '2, A, job')"
    )

class CourseResponse(BaseModel):
    strategy: str = Field(..., description="Selected strategy type")
    message: str = Field(..., description="Human-readable success message")
    output_path: str = Field(..., description="Path to saved course output")
