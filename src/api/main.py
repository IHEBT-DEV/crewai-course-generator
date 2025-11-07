from dotenv import load_dotenv
from fastapi import FastAPI
from src.api.controllers.crew_controller import router as crew_router

load_dotenv()

app = FastAPI(
    title="CrewAI Adaptive Course Generator",
    version="1.0.0",
    description="An adaptive AI-driven course generation API built on CrewAI"
)

# Register routes
app.include_router(crew_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to CrewAI API 🚀",
        "docs": "/docs",
        "health": "/crewai/health"
    }

# Run server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.api.main:app", host="127.0.0.1", port=5000, reload=True)
