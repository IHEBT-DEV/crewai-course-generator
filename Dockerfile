# Note: I removed the first "FROM ubuntu:latest" block as it seemed like a partial copy/paste error.
# The base image is python:3.11-slim, which is correct.

FROM python:3.11-slim AS base
LABEL authors="ihebt"

# ---------- Set working directory ----------
WORKDIR /app

# ---------- Install dependencies ----------
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ---------- Copy project files ----------
# REMOVED: COPY .env .env  <-- This line is gone
COPY ./src ./src

# ---------- Expose FastAPI port ----------
EXPOSE 8000

# ---------- Run the app (Using the CMD from Dockerfile is often cleaner) ----------
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
