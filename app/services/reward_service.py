from sqlalchemy.orm import Session
from ..models.bill import Bill
from ..models.reward import Reward

def check_and_generate_reward(db: Session, user_id: int):
    """Reward user if last 3 bills are paid on or before due date."""
    bills = (
        db.query(Bill)
        .filter(Bill.user_id == user_id)
        .order_by(Bill.due_date.desc())
        .limit(3)
        .all()
    )

    if len(bills) == 3 and all(b.payment_date and b.payment_date <= b.due_date for b in bills):
        reward = Reward(user_id=user_id, reward_type="$10 Amazon Gift Card")
        db.add(reward)
        db.commit()
        db.refresh(reward)
        return reward
    return None
