# app/routers/category.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import WriteCategory, ReadCategory
from app.database import SessionLocal
from app.crud import CRUDCategory

router = APIRouter()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ReadCategory)
async def create_category(category: WriteCategory, db: Session = Depends(get_db)):
    # Create a new category record
    return CRUDCategory.create(db, category)

@router.get("/{category_name}", response_model=ReadCategory)
async def get_category(category_name: str, db: Session = Depends(get_db)):
    category = CRUDCategory.get(db, category_name)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/{category_name}", response_model=ReadCategory)
async def update_category(category_name: str, category: WriteCategory, db: Session = Depends(get_db)):
    try:
        return CRUDCategory.update(db, category_name, category)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{category_name}")
async def delete_category(category_name: str, db: Session = Depends(get_db)):
    try:
        CRUDCategory.delete(db, category_name)
        return {"message": "Category deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
