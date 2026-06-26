# 🧠 CrewAI – Adaptive Course Generator

**CrewAI - Adaptive Course Generator** is an enterprise-ready, multi-agent educational compilation framework built on **FastAPI** and the **CrewAI** orchestration paradigm. 

The framework constructs an adaptive human learning path by deploying an autonomous matrix of up to 20 specialized agents. It balances system payload overhead by using a custom dynamic load-balancing routing layer across multiple free-tier LLM API endpoints.

---

## 🚀 Key Architectural Features

* 🤖 **Hierarchical Multi-Agent Matrix** – Orchestrates up to 20 discrete agents (6 runtime agents per pipeline, classifiers, validators, and integrators) working concurrently.
* ⚡ **Zero-Cost Infra Load Balancing** – Custom routing middleware dynamically balances incoming API payloads across free-tier providers (**SambaNova**, **Nebius**, and **OpenAI**) to prevent runtime token exhaustion.
* 🔄 **Dynamic Strategy Selection** – Automatic input categorization routing traffic down 3 distinct paths: *Academic*, *Hands-On Practical*, or *Comprehensive*.
* 🛡️ **Type-Safe Structured Output** – Guarantees data reliability by enforcing complex, multi-layered Pydantic validation schemas (`Course` model constraints).
* 🐳 **Production Containerized Setup** – Microservices layout wrapped in multi-stage Docker configurations for instant, stateless deployment.

---

## 🏗️ Project Structure

```text
src/
├── api/
│   ├── main.py              # FastAPI application entry point
│   └── routes/              # Explicit REST API endpoint handlers
├── agents/                  # Decoupled YAML structural agent parameters
├── tasks/                   # Decoupled YAML structural task execution parameters
├── strategies/              # Strategy pattern factory mappings and logic
├── models/                  # Pydantic schema engines (Course, Plan, Lesson, etc.)
├── config/                  # Type-safe .env parsing via Pydantic Settings
│   └── settings.py
├── utils/                   # Thread-safe event logging and system helpers
└── crew.py                  # Core Crew orchestration and agent runtime logic
```

---

## ⚙️ Deployment & Installation

### 1️⃣ Clone Environment
```bash
git clone https://github.com
cd adaptive-course-generator
cp .env.example .env
```

### 2️⃣ Configure Environment Variables
Edit your `.env` file to mount your structural credentials:
```env
OPENAI_API_KEY=sk-xxxx
SAMBANOVA_API_KEY=your_sambanova_key
NEBIUS_API_KEY=your_nebius_key
ENVIRONMENT=production
DEBUG=False
```

### 3️⃣ Docker Containerization (Recommended Execution)
```bash
docker compose up --build
```
* The API engine will initialize at: `http://localhost:8000`
* Sanity health validation check: `curl http://localhost:8000/health`

---

## 🧩 Pipeline Agents Overview

| Agent | Operational Purpose | Framework Execution Layer |
| :--- | :--- | :--- |
| **Classifier** | Evaluates user input preferences to determine optimal strategy paths | Pre-Processing Core |
| **Planner** | Generates contextual module flow charts and objective milestones | Context Architecture |
| **Writer** | Compiles granular lesson data arrays and technical content blocks | Content Synthesis |
| **Workshop** | Generates execution challenges, hands-on tasks, and coding projects | Practical Verification |
| **Integrator** | Compiles decoupled asynchronous agent streams into a clean structural JSON | Data Consolidation |

---

## 🧠 Validated Data Models

The system returns a strictly validated `Course` JSON layout containing:

* `title`, `description`, `duration`, `difficulty`
* `plan` – Comprehensive overview mapping module timelines and clear objectives.
* `lessons` – Rigorous technical, conceptual, and theoretical content layers.
* `workshops` – Code challenges, hands-on instructions, and validation tests.
* `strategy_dependent_sections` – Dynamic blocks dependent on selected paths:
  * **Academic Mode**: Deploys deep mathematical proofs, algorithm models, and research paper reviews.
  * **Practical Mode**: Slashes prose to deploy hands-on project builds, test suites, and terminal environments.
  * **Comprehensive Mode**: Balances both frameworks utilizing deep-dive structural real-world case studies.

---

## 💡 REST API Reference

### 1. Health Diagnostic Check
* **Method**: `GET`
* **Endpoint**: `/health`
* **Response**: `{"status": "healthy", "timestamp": "2026-06-27T12:00:00Z"}`

### 2. Streamlined Course Engine Generation
* **Method**: `POST`
* **Endpoint**: `/generate-course`
* **Payload**:
```json
{
  "topic": "Machine Learning Pipelines",
  "user_input": "3 Modules, Advanced, Job Preparation Focus"
}
```
* **Response**:
```json
{
  "course": {
    "title": "Comprehensive Machine Learning Optimization",
    "strategy": "practical_strategy",
    "modules": [...],
    "duration": "~12 hours",
    "difficulty": "Advanced"
  }
}
```

---

## 🧰 Local Development Environment

To construct and run the baseline execution without a Docker daemon:

```bash
# Initialize local runtime environment
python -m venv venv
source venv/bin/activate  # venv\Scripts\activate on Windows
pip install -r requirements.txt

# Run the localized async ASGI server
uvicorn src.api.main:app --host 0.0.5.0 --port 8000 --reload
```

---

## 🧱 Licensing & Terms

Distributed under the MIT License. See `LICENSE` for further operational data permissions.

---

## 🧑‍💻 Technical Point of Contact

* **Lead Systems Architect**: Iheb Touati
* **GitHub Portfolio**: [IHEBT-DEV](https://github.com)
* **Email Gateway**: iheb.touati27@gmail.com
