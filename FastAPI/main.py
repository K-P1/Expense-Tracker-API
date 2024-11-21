from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db import SessionLocal, Base, engine
from schemas import *
from crud import *
from typing import List

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/income/", response_model=ReadIncome)
async def create_income_endpoint(income: WriteIncome, db: Session = Depends(get_db)):
    return create_income(db, income)

@app.post("/expense/", response_model=ReadExpense)
async def create_expense_endpoint(expense: WriteExpense, db: Session = Depends(get_db)):
    return create_expense(db, expense)

@app.post("/category/", response_model=ReadCategory)
async def create_category_endpoint(category: WriteCategory, db: Session = Depends(get_db)):
    return create_category(db, category)


@app.get("/income/{income_id}", response_model=ReadIncome)
async def get_income_endpoint(income_id: int, db: Session = Depends(get_db)):
    income = get_income(db, income_id)
    if income:
        return income
    raise HTTPException(status_code=404, detail="Income not found")

@app.get("/expense/{expense_id}", response_model=ReadExpense)
async def get_expense_endpoint(expense_id: int, db: Session = Depends(get_db)):
    expense = get_expense(db, expense_id)
    if expense:
        return expense
    raise HTTPException(status_code=404, detail="Expense not found")

@app.get("/categories/{category_name}", response_model=ReadCategory)
async def get_category_endpoint(category_name: str, db: Session = Depends(get_db)):
    category = get_category(db, category_name)
    if category:
        return category
    raise HTTPException(status_code=404, detail="Category not found")


@app.get("/expenses/", response_model=List[ReadExpense])
async def get_expenses_endpoint(db: Session = Depends(get_db)):
    return get_expenses(db)

@app.get("/incomes/", response_model=List[ReadIncome])
async def get_incomes_endpoint(db: Session = Depends(get_db)):
    return get_incomes(db)

@app.get('/categories/', response_model=List[ReadCategory])
async def get_categories_endpoint(db: Session = Depends(get_db)):
    return get_categories(db)


@app.delete("/income/{income_id}")
async def delete_income_endpoint(income_id: int, db: Session = Depends(get_db)):
    delete_income(db, income_id)
    return JSONResponse(content={"message": "Income deleted successfully"}, status_code=200)

@app.delete("/expense/{expense_id}")
async def delete_expense_endpoint(expense_id: int, db: Session = Depends(get_db)):
    delete_expense(db, expense_id)
    return JSONResponse(content={"message": "Expense deleted successfully"}, status_code=200)

@app.delete("/category/{category_name}")
async def delete_category_endpoint(category_name: str, db: Session = Depends(get_db)):
    delete_category(db, category_name)
    return JSONResponse(content={"message": "Category deleted successfully"}, status_code=200)
