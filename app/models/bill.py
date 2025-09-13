from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Bill(Base):
    __tablename__ = "bills"

    bill_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    due_date = Column(DateTime, nullable=False)
    payment_date = Column(DateTime, nullable=True)

    user = relationship("User")
