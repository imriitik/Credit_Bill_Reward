from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from ..database import get_db
from ..models.bill import Bill
from ..schemas.bill import Bill as BillSchema, BillCreate
from ..services.reward_service import check_and_generate_reward

router = APIRouter(prefix="/bills", tags=["bills"])

@router.post("/", response_model=BillSchema)
def create_bill(bill: BillCreate, db: Session = Depends(get_db)):
    db_bill = Bill(user_id=bill.user_id, due_date=bill.due_date)
    db.add(db_bill)
    db.commit()
    db.refresh(db_bill)
    return db_bill

@router.get("/{user_id}", response_model=list[BillSchema])
def get_bills(user_id: int, db: Session = Depends(get_db)):
    return db.query(Bill).filter(Bill.user_id == user_id).all()

@router.post("/pay/{bill_id}", response_model=BillSchema)
def pay_bill(bill_id: int, db: Session = Depends(get_db)):
    bill = db.query(Bill).filter(Bill.bill_id == bill_id).first()
    if not bill:
        raise HTTPException(status_code=404, detail="Bill not found")
    if bill.payment_date:
        raise HTTPException(status_code=400, detail="Bill already paid")

    bill.payment_date = datetime.utcnow()
    db.commit()
    db.refresh(bill)

    check_and_generate_reward(db, bill.user_id)
    return bill
