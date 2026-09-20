# AI Service — `ai-service/`

Python + FastAPI microservice providing AI capabilities for FitFlow.

## Planned structure

```
ai-service/
├── app/
│   ├── main.py               # FastAPI application entrypoint
│   ├── api/                  # REST endpoints
│   ├── recommendation/       # Recommendation engine (personalized suggestions)
│   ├── vision/               # Computer vision (pose estimation, form analysis)
│   └── schemas/              # Pydantic models
├── tests/
├── requirements.txt
└── Dockerfile
```

## Tech

- Python + FastAPI (Pydantic, OpenAPI docs)
- Recommendation engine: scikit-learn / PyTorch
- Computer vision: OpenCV + YOLO / MediaPipe
- Uvicorn + Gunicorn serving

## Getting started

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

> This folder is scaffolded; model and endpoint code is added as part of the redesign.
