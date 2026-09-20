# Comparison Matrix

This matrix documents the options evaluated for each major technology decision in the FitFlow redesign. ✅ marks the selected option.

## Frontend framework

| Option | iOS + Android | Web support | Language | Ecosystem | Team familiarity | Decision |
|--------|:---:|:---:|----------|-----------|:---:|:---:|
| React Native (Expo) | ✅ | ✅ (RN Web) | TypeScript | Large | High | ✅ **Chosen** |
| Flutter | ✅ | ✅ | Dart | Large | Low | — |
| Native (Swift/Kotlin) | ✅ | ❌ (separate) | Swift/Kotlin | Mature | Low | — |
| React + Capacitor | ✅ | ✅ | TypeScript | Large | Medium | — |

## Backend framework

| Option | Language | Structure | Performance | Ecosystem | TypeScript | Decision |
|--------|----------|-----------|-------------|-----------|:---:|:---:|
| NestJS | Node/TS | Modular, DI | Good (async I/O) | Large | ✅ | ✅ **Chosen** |
| Express | Node/JS | Minimal | Good | Huge | ✅ | — |
| Fastify | Node/TS | Minimal | Excellent | Medium | ✅ | — |
| Spring Boot | Java | Modular | Excellent | Mature | ❌ | — |
| Django | Python | Batteries-included | Good | Large | ❌ | — |

## AI service framework

| Option | Language | ML ecosystem | Computer vision | Async/typed | Decision |
|--------|----------|--------------|-----------------|-------------|:---:|
| FastAPI | Python | ✅ (sklearn/PyTorch/TF) | ✅ (OpenCV/YOLO) | ✅ | ✅ **Chosen** |
| Flask | Python | ✅ | ✅ | ❌ | — |
| TensorFlow.js | JS | Limited | Limited | — | — |
| TorchServe | Python | ✅ (PyTorch) | Limited | ❌ | — |

## Primary database

| Option | Type | Consistency | JSON support | Tooling | Decision |
|--------|------|:---:|:---:|---------|:---:|
| PostgreSQL | Relational | Strong | ✅ (JSONB) | Excellent | ✅ **Chosen** |
| MongoDB | Document | Eventual | ✅ (native) | Good | — |
| MySQL | Relational | Strong | Partial | Good | — |
| DynamoDB | NoSQL (KV/Doc) | Tunable | ✅ | Good (AWS) | — |

## Architecture: legacy vs. redesigned

| Aspect | Legacy (monolith) | Redesigned (services) |
|--------|-------------------|-----------------------|
| Deployment | Single unit | Independent services |
| Scaling | Scale everything together | Scale per service (e.g. AI vs. social) |
| AI workloads | Coupled to app server | Isolated Python microservice |
| Technology fit | One language for all | Polyglot (TS + Python) |
| Failure blast radius | Whole app | Isolated to one service |
| Operational complexity | Low | Higher (orchestration, tracing) |
| Time-to-market for a feature | Fast initially | Fast per-service, more coordination |

## Recommendation

The selected options (React Native + NestJS + FastAPI + PostgreSQL) maximize ecosystem
maturity, TypeScript/Python fit for their domains, and team familiarity while keeping the
operational surface manageable for a small team.
