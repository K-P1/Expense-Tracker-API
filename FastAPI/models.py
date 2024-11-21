from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey, func
from sqlalchemy.orm import relationship
from db import Base

class Income(Base):
    __tablename__ = 'incomes'
    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    currency = Column(String, default="NGN")
    date = Column(Date, default=func.current_date())
    time = Column(Time, default=func.current_time())
    description = Column(String)

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    currency = Column(String, default="NGN")
    date = Column(Date, default=func.current_date())
    time = Column(Time, default=func.current_time())
    description = Column(String)
    category_name = Column(String, ForeignKey('categories.name'), nullable=True)
    category = relationship("Category", back_populates="expenses")

class Category(Base):
    __tablename__ = 'categories'
    name = Column(String, primary_key=True, unique=True)
    description = Column(String)
    expenses = relationship("Expense", back_populates="category")
