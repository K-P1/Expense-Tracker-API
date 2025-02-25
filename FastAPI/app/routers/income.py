# app/routers/income.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import WriteIncome, ReadIncome
from app.database import SessionLocal
from app.crud import CRUDIncome

router = APIRouter()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ReadIncome)
async def create_income(income: WriteIncome, db: Session = Depends(get_db)):
    # Create a new income record
    return CRUDIncome.create(db, income)

@router.get("/{income_id}", response_model=ReadIncome)
async def get_income(income_id: int, db: Session = Depends(get_db)):
    income = CRUDIncome.get(db, income_id)
    if income is None:
        raise HTTPException(status_code=404, detail="Income not found")
    return income

@router.put("/{income_id}", response_model=ReadIncome)
async def update_income(income_id: int, income: WriteIncome, db: Session = Depends(get_db)):
    try:
        return CRUDIncome.update(db, income_id, income)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{income_id}")
async def delete_income(income_id: int, db: Session = Depends(get_db)):
    try:
        CRUDIncome.delete(db, income_id)
        return {"message": "Income deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
