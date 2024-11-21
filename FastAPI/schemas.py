#SCHEMAS.PY
from pydantic import BaseModel
from typing import Optional, List, TYPE_CHECKING
from datetime import date as dt_date, time as dt_time

if TYPE_CHECKING:
    from .schemas import ReadExpense  # Forward reference for type checking

class WriteIncome(BaseModel):
    amount: int
    description: str
    date: Optional[dt_date] =  None

class WriteExpense(BaseModel):
    amount: int
    description: str
    category_name: Optional[str]
    date: Optional[dt_date] =  None

class WriteCategory(BaseModel):
    name: str
    description: str

class ReadIncome(BaseModel):
    id: int
    amount: int
    currency: str
    description: str
    date: Optional[dt_date]
    time: Optional[dt_time]

    class Config:
        orm_mode = True

class ReadCategory(BaseModel):
    name: str
    description: str
    expenses: List["ReadExpense"] = []  # Forward reference for nested relationships

    class Config:
        orm_mode = True

    def dict(self, **kwargs):
        kwargs['exclude_unset'] = True  # Prevent recursion by excluding unset fields
        return super().model_dump(**kwargs)

class ReadExpense(BaseModel):
    id: int
    amount: int
    currency: str
    description: str
    date: Optional[dt_date]
    time: Optional[dt_time]
    category_name: Optional[str]  # Avoid deep nesting by using just the name

    class Config:
        orm_mode = True

    def dict(self, **kwargs):
        kwargs['exclude_unset'] = True  # Prevent recursion by excluding unset fields
        return super().model_dump(**kwargs)

class Report(BaseModel):
    start_date: dt_date
    end_date: dt_date

    class Config:
        orm_mode = True

# Resolve forward references for nested relationships
ReadCategory.model_rebuild()
ReadExpense.model_rebuild()