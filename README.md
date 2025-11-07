# 🧠 CrewAI – Adaptive Course Generator

**CrewAI** is an intelligent, multi-agent educational content generator built on **FastAPI** and **CrewAI**.  
It uses LLM agents (Planner, Writer, Workshop, Integrator, etc.) to automatically produce well-structured, adaptive learning courses based on user input and learning preferences.

---

## 🚀 Features

✅ **Multi-Agent Architecture** – Planner, Writer, Workshop, Integrator, and Classifier agents working collaboratively  
✅ **Dynamic Strategy Selection** – Academic, Practical, or Comprehensive strategies selected automatically  
✅ **Structured Output** – Generates a unified `Course` model with plans, lessons, workshops, exercises, and resources  
✅ **API-first Design** – Exposed as a RESTful API using FastAPI  
✅ **Dockerized** – Fully containerized for consistent deployment  
✅ **.env Configuration** – Centralized, type-safe configuration system  
✅ **Scalable Logging & Modularity** – Clean logging and modular architecture  

---

## 🏗️ Project Structure

src/
├── agents/ # YAML agent definitions
├── tasks/ # YAML task definitions
├── strategies/ # Strategy factory and configurations
├── utils/ # Logging, helpers, and other utilities
├── models/ # Pydantic models (Course, Plan, Lesson, etc.)
├── api/
│ ├── main.py # FastAPI entry point
│ └── routes/ # API routes
├── config/
│ └── settings.py # .env loader and app configuration
└── crew.py # Crew orchestration logic (builds and runs crews)


---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/crewai.git
cd crewai
2️⃣ Create and configure your environment
Copy the example environment file:

cp .env.example .env
Then edit .env to include your API keys and configuration:

OPENAI_API_KEY=sk-xxxx
SAMBANOVA_API_KEY=your_sambanova_key
NEBIUS_API_KEY=your_nebius_key
ENVIRONMENT=production
DEBUG=False
🐳 Run with Docker (Recommended)
Build and start the container:

docker compose up --build
The API will be available at:


http://localhost:8000
Check health:
curl http://localhost:8000/health
💡 API Endpoints
Method	Endpoint	Description
GET	/health	Health check endpoint
POST	/generate-course	Generate a new course based on topic and user input (future)
GET	/crewai/test	Test route

(More endpoints can be added easily in src/api/routes/.)

🧩 Agents Overview
| Agent          | Purpose                                                                    |
| :------------- | :------------------------------------------------------------------------- |
| **Classifier** | Determines the best learning strategy (academic, practical, comprehensive) |
| **Planner**    | Designs the course structure and flow                                      |
| **Writer**     | Generates individual lessons and learning content                          |
| **Workshop**   | 3 for each strategy (mixed exercises, hand-on tasks, project buildong...   |                               |
| **Integrator** | Merges all components into a unified, coherent course output               |


🧠 Course Model
The Course model includes:

title, description

plan (overview, modules, objectives)

lessons (theoretical content)

workshops (practical exercises)

resources (books, articles, videos)

key_takeaways

strategy-dependent sections:

Academic: algorithm implementations, paper analyses, theoretical exercises

Practical: code challenges, hands-on exercises, project building

Comprehensive: case studies, mini-projects, mixed exercises

🧰 Local Development
If you prefer to run without Docker:

Install dependencies
pip install -r requirements.txt
Run the app
uvicorn src.api.main:app --reload
🧾 Example Run
Interactive CLI mode:


python src/crew.py
API mode:
curl -X POST http://localhost:8000/generate-course \
  -H "Content-Type: application/json" \
  -d '{"topic": "Machine Learning", "user_input": "3, A, job"}'
Example response:

{
  "course": {
    "title": "Comprehensive Machine Learning Course",
    "strategy": "practical_strategy",
    "modules": [...],
    "duration": "~12 hours",
    "difficulty": "Intermediate"
  }
}
🧩 Tech Stack
Python 3.11+

FastAPI – Web framework

CrewAI – Multi-agent orchestration

Pydantic – Data validation

Docker + Docker Compose – Containerization

Uvicorn – ASGI server

🛡️ Environment Variables
| Variable            | Description                  | Example                      |
| :------------------ | :--------------------------- | :--------------------------- |
| `OPENAI_API_KEY`    | API key for OpenAI models    | `sk-xxxx`                    |
| `SAMBANOVA_API_KEY` | API key for SambaNova models | `xxxx`                       |
| `NEBIUS_API_KEY`    | API key for Nebius models    | `xxxx`                       |
| `DEBUG`             | Enable FastAPI debug mode    | `True`                       |
| `ENVIRONMENT`       | App environment              | `production` / `development` |


🧑‍💻 Development Notes
Configuration is centralized in src/config/settings.py

All logs are managed by src/utils/logging_utils.py

Strategies and agents are declared in YAML for modular updates

Outputs are stored under /outputs

🧱 License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute with attribution.

💬 Contact
Maintainer: IT
📧 Email: iheb.touati27@gmail.com