# Backend — `backend/`

Node.js + NestJS services for the FitFlow redesign.

## Planned structure (modular monorepo → services)

```
backend/
├── apps/
│   ├── api-gateway/    # BFF / API Gateway
│   ├── auth/           # Identity, sessions, OAuth2/OIDC
│   ├── workout/        # Exercise plans, logging, progress
│   ├── nutrition/      # Meal tracking, macros, diet plans
│   └── social/         # Feeds, follows, activity sharing
├── libs/               # Shared NestJS libraries (config, prisma, guards)
└── package.json
```

## Tech

- Node.js + NestJS + TypeScript
- Prisma ORM (PostgreSQL)
- JWT + OAuth2/OIDC auth
- RabbitMQ for async events

## Getting started

```bash
npm install
npm run start:dev   # start dev server
```

> This folder is scaffolded; service code is added as part of the redesign.
