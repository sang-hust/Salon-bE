import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.database.session import engine
from app.database.base import Base
from app.api.v1 import appointments as appointments_router

# Import models so that metadata creates tables
from app.models import user  # noqa

from app.api.v1 import auth as auth_router
from app.api.v1 import health as health_router
from app.api.v1 import staff as staff_router
from app.api.v1 import slots as slots_router
from app.api.v1 import products as products_router
app = FastAPI(title=settings.app_name)

# CORS (allow your React dev server)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create DB tables (for simple dev setup; use Alembic for prod)
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(health_router.router, prefix="/api/v1", tags=["Health"])
app.include_router(auth_router.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(health_router.router, prefix="/api/v1", tags=["Health"])
app.include_router(auth_router.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(staff_router.router, prefix="/api/v1/staff", tags=["Staff"])
app.include_router(slots_router.router, prefix="/api/v1/slots", tags=["Slots"])
app.include_router(products_router.router, prefix="/api/v1/products", tags=["Products"])
app.include_router(appointments_router.router, prefix="/api/v1", tags=["Appointments"])