from sqlalchemy.orm import Session
from app import models
from app.schemas import user
from app.core.security import get_password_hash


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user_in: user.UserCreate):
    hashed = get_password_hash(user_in.password)
    db_user = models.User(email=user_in.email, hashed_password=hashed, full_name=user_in.full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user