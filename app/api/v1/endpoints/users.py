from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import crud
from app.schemas import user
from app.api import deps

router = APIRouter()

@router.post("/", response_model=user.UserRead)
def create_user(user_in: user.UserCreate, db: Session = Depends(deps.get_db)):
    user_obj = crud.get_user_by_email(db, email=user_in.email)
    if user_obj:
        raise HTTPException(status_code=400, detail="Email already registered")
    created = crud.create_user(db, user_in=user_in)
    return created

@router.get("/me", response_model=user.UserRead)
def read_users_me(current_user: user.UserRead = Depends(deps.get_current_user)):
    return current_user