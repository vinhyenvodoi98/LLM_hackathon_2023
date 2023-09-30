# {App name}

## Build image
### Backend
1. Build backend image
```bash
cd backend/
docker build .
```

### Frontend

## Run
1. Copy `.env.example` and change env variable as you like
```bash
cd ${root_project_folder}
cp .env.example .env
```
2. Run docker compose
```bash
docker-compose up -d
```