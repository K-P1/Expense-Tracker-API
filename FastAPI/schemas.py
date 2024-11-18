from pydantic import BaseModel
from typing import Optional, List, TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from .schemas import ReadExpense  # Forward reference for type checking

class WriteIncome(BaseModel):
    amount: int
    description: str

class WriteExpense(BaseModel):
    amount: int
    description: str
    category_name: Optional[str]

class WriteCategory(BaseModel):
    name: Optional[str]
    description: Optional[str]

class ReadIncome(BaseModel):
    id: int
    amount: int
    currency: str
    description: str
    date_time: Optional[str]

    class Config:
        orm_mode = True

class ReadCategory(BaseModel):
    id: int
    name: str
    description: str
    expenses: List["ReadExpense"] = []  # Use forward reference for nested relationships

    class Config:
        orm_mode = True

class ReadExpense(BaseModel):
    id: int
    amount: int
    currency: str
    date_time: str
    description: str
    category_name: Optional[str]
    category: Optional[ReadCategory]  # Use forward reference for circular dependency

    class Config:
        orm_mode = True

class Report(BaseModel):
    start_date: date
    end_date: date

    class Config:
        orm_mode = True