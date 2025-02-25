# app/schemas.py
from pydantic import BaseModel, ConfigDict
from typing import Optional, List, TYPE_CHECKING
from datetime import date as dt_date, time as dt_time

if TYPE_CHECKING:
    from .schemas import ReadExpense  # For type checking nested relationships

# Input schema for Income
class WriteIncome(BaseModel):
    amount: int
    description: str
    date: Optional[dt_date] = None

# Input schema for Expense
class WriteExpense(BaseModel):
    amount: int
    description: str
    category_name: Optional[str]
    date: Optional[dt_date] = None

# Input schema for Category
class WriteCategory(BaseModel):
    name: str
    description: str

# Output schema for Income
class ReadIncome(BaseModel):
    id: int
    amount: int
    currency: str
    description: str
    date: Optional[dt_date]
    time: Optional[dt_time]

    model_config = ConfigDict(from_attributes=True)



# Output schema for Category with nested expenses
class ReadCategory(BaseModel):
    name: str
    description: str
    expenses: List["ReadExpense"] = []  # Forward reference for nested expenses

    class ConfigDict:
        from_attributes = True

    def dict(self, **kwargs):
        kwargs['exclude_unset'] = True  # Avoid recursive unset fields
        return super().model_dump(**kwargs)

# Output schema for Expense
class ReadExpense(BaseModel):
    id: int
    amount: int
    currency: str
    description: str
    date: Optional[dt_date]
    time: Optional[dt_time]
    category_name: Optional[str]  # Only include category name

    class ConfigDict:
        from_attributes = True

    def dict(self, **kwargs):
        kwargs['exclude_unset'] = True  # Avoid recursion issues
        return super().model_dump(**kwargs)

# Schema for report request
class Report(BaseModel):
    start_date: dt_date
    end_date: dt_date

    class ConfigDict:
        from_attributes = True

# Schema for full report response
class ReadReport(BaseModel):
    date_range: str
    currency: str
    total_credit: int
    total_debit: int
    total_income: int
    total_expense: int
    start_balance: int
    end_balance: int
    incomes: List[ReadIncome]
    expenses: List[ReadExpense]

    class ConfigDict:
        from_attributes = True

# Schema for summary report response
class ReadSummary(BaseModel):
    date_range: str
    currency: str
    total_credit: int
    total_debit: int
    total_income: int
    total_expense: int
    start_balance: int
    end_balance: int

    class ConfigDict:
        from_attributes = True

# Resolve forward references for nested relationships
ReadCategory.model_rebuild()
ReadExpense.model_rebuild()
