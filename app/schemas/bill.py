from pydantic import BaseModel
from datetime import datetime

class BillBase(BaseModel):
    user_id: int
    due_date: datetime

class BillCreate(BillBase):
    pass

class Bill(BillBase):
    bill_id: int
    payment_date: datetime | None

    class Config:
        orm_mode = True
