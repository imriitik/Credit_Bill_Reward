from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.user import User
from ..schemas.user import UserCreate, User as UserSchema

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/all_users", response_model=list[UserSchema])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()
