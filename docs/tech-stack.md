# Tech Stack Summary

This document summarizes the technology choices for the FitFlow redesign and the rationale behind each one.

## Frontend — `frontend/`

| Concern | Choice | Rationale |
|---------|--------|-----------|
| Framework | React Native (Expo) | Single TypeScript codebase for iOS, Android, and web; fast iteration via Expo |
| Web target | React (React Native Web) | Shares components/business logic with the mobile app |
| Language | TypeScript | Static typing, shared types with the NestJS backend |
| State | React Query + Zustand | Server-state caching and lightweight client state |
| Navigation | Expo Router | File-based routing that mirrors web conventions |

## Backend — `backend/`

| Concern | Choice | Rationale |
|---------|--------|-----------|
| Runtime | Node.js (LTS) | Large ecosystem, fast I/O, TypeScript-native |
| Framework | NestJS | Opinionated, modular architecture with DI — maps cleanly to microservices |
| Services | auth, workout, nutrition, social | Each bounded context is an independently deployable module |
| API style | REST (OpenAPI) + gRPC internally | Public REST contracts, low-latency internal calls |
| ORM | Prisma | Type-safe queries, migrations, multi-service schema management |
| Auth | JWT + OAuth2 (OIDC) | Stateless, interoperable with social login |

## AI Service — `ai-service/`

| Concern | Choice | Rationale |
|---------|--------|-----------|
| Language | Python | Dominant ML/data-science ecosystem |
| Framework | FastAPI | Async, typed (Pydantic), automatic OpenAPI docs |
| Recommendation engine | scikit-learn / PyTorch | Classical models first, deep models where uplift justifies it |
| Computer vision | OpenCV + YOLO / MediaPipe | Pose estimation and form analysis for workouts |
| Serving | Uvicorn + Gunicorn | Production-grade ASGI serving |

## Data & Infrastructure

| Concern | Choice | Rationale |
|---------|--------|-----------|
| Primary database | PostgreSQL | Relational integrity, JSONB flexibility, mature tooling |
| Cache / sessions | Redis | Sub-ms reads, rate limiting, pub/sub |
| Message bus | RabbitMQ | Reliable async communication between services and AI |
| Object storage | S3-compatible | Storing images, videos, and trained model artifacts |
| Containerization | Docker | Consistent environments across services |
| CI/CD | GitHub Actions | Native to GitHub, simple multi-job pipelines |

## Cross-cutting concerns

- **Observability** — OpenTelemetry for traces/metrics, structured JSON logs.
- **Security** — least-privilege service accounts, secret management, OWASP checks in CI.
- **Testing** — unit + integration tests per service, contract tests at service boundaries.
