from fastapi import FastAPI
from app.api.v1.endpoints import auth, users
from app.db import base  # make sure models are imported for alembic autogenerate
from app.db.session import engine
from app.core.config import settings

# Create all tables (for dev only; prefer Alembic in production)
from app.db.base import Base
# Import models after Base is defined to avoid circular imports
from app.models.user import User  # noqa
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI + MySQL + JWT Example")

api_v1_router = FastAPI()

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])

@app.get("/")
def root():
    return {"message": "Hello World"}