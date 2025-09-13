from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.reward import Reward
from ..schemas.reward import Reward as RewardSchema

router = APIRouter(prefix="/rewards", tags=["rewards"])

@router.get("/{user_id}", response_model=list[RewardSchema])
def get_rewards(user_id: int, db: Session = Depends(get_db)):
    return db.query(Reward).filter(Reward.user_id == user_id).all()
