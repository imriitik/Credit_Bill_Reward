from pydantic import BaseModel

class RewardBase(BaseModel):
    user_id: int
    reward_type: str

class Reward(RewardBase):
    reward_id: int

    class Config:
        orm_mode = True
