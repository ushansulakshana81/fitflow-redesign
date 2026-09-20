# Frontend — `frontend/`

React Native (Expo) application targeting **iOS, Android, and web**.

## Planned structure

```
frontend/
├── app/              # Expo Router screens (file-based routing)
├── components/       # Reusable UI components
├── features/         # Feature modules (workout, nutrition, social)
├── hooks/            # Shared hooks
├── services/         # API client and data fetching
├── state/            # Zustand stores
├── theme/            # Design tokens and theming
├── app.json          # Expo config
└── package.json
```

## Tech

- React Native (Expo) + TypeScript
- React Native Web (web target)
- Expo Router, React Query, Zustand

## Getting started

```bash
npm install
npm start          # start Expo dev server
npm run web        # start web target
```

> This folder is scaffolded; application code is added as part of the redesign.
