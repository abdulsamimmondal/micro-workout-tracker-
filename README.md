# 🏋️ Micro Workout Tracker

A lightweight microservice to log and track quick workouts using FastAPI and PostgreSQL. Deployed on AWS EKS.

---

## 📦 Features

- FastAPI-based REST API
- PostgreSQL via Amazon RDS
- Containerized with Docker
- Kubernetes deployment-ready (EKS)
- LoadBalanced service for public access

---

## 🗃️ API Endpoints

| Method | Endpoint              | Description                   |
|--------|-----------------------|-------------------------------|
| POST   | `/workouts/`          | Add a new workout             |
| GET    | `/workouts/`          | List all workouts             |
| GET    | `/workouts/today`     | Workouts logged today         |
| GET    | `/workouts/{id}`      | Get a specific workout by ID  |
| DELETE | `/workouts/{id}`      | Delete a workout              |

---

## 🚀 Quick Start (Local)

```bash
# Create virtual environment
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export DB_HOST=localhost
export DB_USER=postgres
export DB_PASSWORD=yourpassword
export DB_NAME=workoutdb

# Run the server
uvicorn app.main:app --reload
