# app/main.py
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import income, expense, category, report
from app.utils.logger import logger

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers for modular endpoints
app.include_router(income.router, prefix="/income", tags=["income"])
app.include_router(expense.router, prefix="/expense", tags=["expense"])
app.include_router(category.router, prefix="/category", tags=["category"])
app.include_router(report.router, prefix="/report", tags=["report"])

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the Financial API"}
