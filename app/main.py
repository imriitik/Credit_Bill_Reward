from fastapi import FastAPI
from .database import Base, engine
from .routes import users, bills, rewards

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="BON Rewards API", version="1.0.0")

# Routers
app.include_router(users.router)
app.include_router(bills.router)
app.include_router(rewards.router)

@app.get("/")
def root():
    return {"message": "Welcome to BON Rewards API"}
