from typing import List, Optional
from pydantic import BaseModel, Field

# ============================================================
# 🔹 Supporting Models
# ============================================================

class Resources(BaseModel):
    """Supporting resources, readings, and learning aids."""
    books: Optional[List[str]] = Field(default_factory=list, description="List of recommended books")
    articles: Optional[List[str]] = Field(default_factory=list, description="List of reference articles or papers")
    videos: Optional[List[str]] = Field(default_factory=list, description="Video tutorials or lectures")
    websites: Optional[List[str]] = Field(default_factory=list, description="Useful websites or online tools")


class Plan(BaseModel):
    """Structured course plan defining modules and objectives."""
    overview: str = Field(..., description="General overview of the course structure")
    modules: List[str] = Field(..., description="List of main modules or topics")
    learning_objectives: Optional[List[str]] = Field(default_factory=list, description="Learning objectives for the course")


class Lesson(BaseModel):
    """Individual lesson structure."""
    title: str = Field(..., description="Title of the lesson")
    content: str = Field(..., description="Lesson content or narrative")
    objectives: Optional[List[str]] = Field(default_factory=list, description="Lesson-specific objectives")
    summary: Optional[str] = Field(None, description="Brief summary of the lesson")


class Workshop(BaseModel):
    """Hands-on or practical workshop structure."""
    title: str = Field(..., description="Workshop title")
    description: str = Field(..., description="Description of the workshop session")
    exercises: Optional[List[str]] = Field(default_factory=list, description="Exercises or activities included")
    outcomes: Optional[List[str]] = Field(default_factory=list, description="Expected learning outcomes from the workshop")

# ============================================================
# 🔸 Specialized Learning Structures
# ============================================================

class AlgorithmImplementation(BaseModel):
    """Implementation-focused exercises related to algorithms."""
    title: str = Field(..., description="Title of the implementation exercise")
    description: str = Field(..., description="Explanation of the algorithm or implementation goal")
    code_snippets: Optional[List[str]] = Field(default_factory=list, description="Code snippets or examples")
    expected_outcomes: Optional[List[str]] = Field(default_factory=list, description="Expected learning outcomes or results")


class PaperAnalysis(BaseModel):
    """Analysis of academic or research papers."""
    paper_title: str = Field(..., description="Title of the analyzed paper")
    authors: Optional[List[str]] = Field(default_factory=list, description="Authors of the paper")
    key_concepts: Optional[List[str]] = Field(default_factory=list, description="Key ideas and findings from the paper")
    critical_analysis: str = Field(..., description="Critical review or commentary on the paper")
    related_topics: Optional[List[str]] = Field(default_factory=list, description="Related theories or techniques")


class TheoreticalExercises(BaseModel):
    """Conceptual or theory-driven exercises."""
    title: str = Field(..., description="Exercise title")
    questions: List[str] = Field(..., description="Theoretical questions to solve")
    objectives: Optional[List[str]] = Field(default_factory=list, description="Learning goals of the exercise")
    solutions: Optional[List[str]] = Field(default_factory=list, description="Optional example solutions or hints")


class CodeChallenges(BaseModel):
    """Coding challenges or competitive-style tasks."""
    title: str = Field(..., description="Challenge title")
    description: str = Field(..., description="Description of the challenge")
    input_output_examples: Optional[List[str]] = Field(default_factory=list, description="Example input/output scenarios")
    difficulty: Optional[str] = Field(None, description="Difficulty level (e.g., easy, medium, hard)")
    solution_guides: Optional[List[str]] = Field(default_factory=list, description="Guidance or hints for solving the challenge")


class HandsOnExercises(BaseModel):
    """Applied exercises with practical implementation."""
    title: str = Field(..., description="Exercise title")
    description: str = Field(..., description="Exercise goal and context")
    steps: Optional[List[str]] = Field(default_factory=list, description="Step-by-step instructions for execution")
    expected_results: Optional[List[str]] = Field(default_factory=list, description="Expected outputs or achievements")


class ProjectBuilding(BaseModel):
    """Guided projects for deep learning by doing."""
    title: str = Field(..., description="Project title")
    description: str = Field(..., description="Brief project description")
    milestones: Optional[List[str]] = Field(default_factory=list, description="Major project milestones")
    tools_required: Optional[List[str]] = Field(default_factory=list, description="Tools or frameworks required")
    deliverables: Optional[List[str]] = Field(default_factory=list, description="Final deliverables or results")


class CaseStudy(BaseModel):
    """Detailed case studies of real-world applications."""
    title: str = Field(..., description="Case study title")
    context: str = Field(..., description="Description of the real-world scenario or company")
    analysis: str = Field(..., description="Detailed analysis and insights")
    lessons_learned: Optional[List[str]] = Field(default_factory=list, description="Key takeaways or lessons from the case")


class MiniProjects(BaseModel):
    """Short and focused projects."""
    title: str = Field(..., description="Mini-project title")
    description: str = Field(..., description="What the project covers")
    duration: Optional[str] = Field(None, description="Estimated completion time")
    goals: Optional[List[str]] = Field(default_factory=list, description="Learning goals or expected outcomes")
    deliverables: Optional[List[str]] = Field(default_factory=list, description="Project outputs")


class MixedExercises(BaseModel):
    """A combination of theoretical and practical exercises."""
    title: str = Field(..., description="Exercise title")
    theory_part: str = Field(..., description="Theoretical background")
    practice_part: str = Field(..., description="Practical implementation or application")
    questions: Optional[List[str]] = Field(default_factory=list, description="Associated questions or reflections")

# ============================================================
# 🧠 Unified Final Course Output
# ============================================================

class Course(BaseModel):
    """Unified course output integrating academic content, resources, and workshops."""
    title: str = Field(..., description="Final course title")
    description: Optional[str] = Field(None, description="General description of the course")
    plan: Plan = Field(..., description="Structured course plan")
    lessons: Optional[List[Lesson]] = Field(default_factory=list, description="Comprehensive lesson list from the writer agents")
    workshops: Optional[List[Workshop]] = Field(default_factory=list, description="Workshop session summaries")
    resources: Optional[Resources] = Field(default_factory=Resources, description="Recommended readings and learning aids")
    key_takeaways: Optional[List[str]] = Field(default_factory=list, description="Main insights or skills gained from the course")


class AcademicFullCourse(BaseModel):
    """Unified course output integrating academic content, resources, and workshops."""
    title: str = Field(..., description="Final course title")
    description: Optional[str] = Field(None, description="General description of the course")
    plan: Plan = Field(..., description="Structured course plan")
    lessons: Optional[List[Lesson]] = Field(default_factory=list, description="Comprehensive lesson list from the writer agents")
    workshops: Optional[List[Workshop]] = Field(default_factory=list, description="Workshop session summaries")
    resources: Optional[Resources] = Field(default_factory=Resources, description="Recommended readings and learning aids")
    key_takeaways: Optional[List[str]] = Field(default_factory=list, description="Main insights or skills gained from the course")

    # 🔸 Advanced and applied content
    algorithm_implementations: Optional[List[AlgorithmImplementation]] = Field(default_factory=list, description="Algorithm coding and implementation exercises")
    paper_analyses: Optional[List[PaperAnalysis]] = Field(default_factory=list, description="Critical reviews and paper studies")
    theoretical_exercises: Optional[List[TheoreticalExercises]] = Field(default_factory=list, description="Theory-driven exercises and problem sets")

class PracticalFullCourse(BaseModel):
    """Unified course output integrating academic content, resources, and workshops."""
    title: str = Field(..., description="Final course title")
    description: Optional[str] = Field(None, description="General description of the course")
    plan: Plan = Field(..., description="Structured course plan")
    lessons: Optional[List[Lesson]] = Field(default_factory=list, description="Comprehensive lesson list from the writer agents")
    workshops: Optional[List[Workshop]] = Field(default_factory=list, description="Workshop session summaries")
    resources: Optional[Resources] = Field(default_factory=Resources, description="Recommended readings and learning aids")
    key_takeaways: Optional[List[str]] = Field(default_factory=list, description="Main insights or skills gained from the course")

    code_challenges: Optional[List[CodeChallenges]] = Field(default_factory=list,
                                                            description="Coding challenge collection")
    hands_on_exercises: Optional[List[HandsOnExercises]] = Field(default_factory=list,
                                                                 description="Practical exercises and applications")
    project_building: Optional[List[ProjectBuilding]] = Field(default_factory=list,
                                                              description="Full-scale guided projects")


class ComprehensiveFullCourse(BaseModel):
    """Unified course output integrating academic content, resources, and workshops."""
    title: str = Field(..., description="Final course title")
    description: Optional[str] = Field(None, description="General description of the course")
    plan: Plan = Field(..., description="Structured course plan")
    lessons: Optional[List[Lesson]] = Field(default_factory=list,
                                            description="Comprehensive lesson list from the writer agents")
    workshops: Optional[List[Workshop]] = Field(default_factory=list, description="Workshop session summaries")
    resources: Optional[Resources] = Field(default_factory=Resources,
                                           description="Recommended readings and learning aids")
    key_takeaways: Optional[List[str]] = Field(default_factory=list,
                                               description="Main insights or skills gained from the course")

    case_studies: Optional[List[CaseStudy]] = Field(default_factory=list,
                                                    description="Real-world case studies and analysis")
    mini_projects: Optional[List[MiniProjects]] = Field(default_factory=list, description="Short, focused projects")
    mixed_exercises: Optional[List[MixedExercises]] = Field(default_factory=list,
                                                            description="Exercises mixing theory and practice")
