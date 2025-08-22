# FastAPI Backend for Salon Booking (Auth-First)

This is a clean, extensible FastAPI backend skeleton with JWT auth,
ready to plug into your React landing page. It is organized with clean
layers (API / Services / Repositories / Models).

## Quickstart

```bash
python -m venv .venv
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt

# Copy env and edit SECRET_KEY if needed
cp .env.example .env  # Windows: copy .env.example .env

# Run dev server
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs to try the API.

### Auth endpoints

- POST `/api/v1/auth/register`  (body: username, email, password) -> returns access token
- POST `/api/v1/auth/login`     (body: email, password) -> returns access token
- GET  `/api/v1/auth/me`        (Authorization: Bearer <token>) -> returns current user

CORS allows http://localhost:5173 and :3000 by default (adjust in `app/main.py`).

## Next steps

- Add Staff/Slots/Bookings modules (models, repositories, services, api)
- Switch SQLite to PostgreSQL by changing `DATABASE_URL` in `.env`
- Add Alembic migrations for production
- Add role-based authorization (admin vs user) in deps
