from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Reward(Base):
    __tablename__ = "rewards"

    reward_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    reward_type = Column(String, nullable=False)

    user = relationship("User")
