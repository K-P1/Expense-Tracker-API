# app/routers/expense.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import WriteExpense, ReadExpense
from app.database import SessionLocal
from app.crud import CRUDEexpense

router = APIRouter()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ReadExpense)
async def create_expense(expense: WriteExpense, db: Session = Depends(get_db)):
    # Create a new expense record
    return CRUDEexpense.create(db, expense)

@router.get("/{expense_id}", response_model=ReadExpense)
async def get_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = CRUDEexpense.get(db, expense_id)
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

@router.put("/{expense_id}", response_model=ReadExpense)
async def update_expense(expense_id: int, expense: WriteExpense, db: Session = Depends(get_db)):
    try:
        return CRUDEexpense.update(db, expense_id, expense)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{expense_id}")
async def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    try:
        CRUDEexpense.delete(db, expense_id)
        return {"message": "Expense deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
