import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class Income(Base):
    __tablename__ = 'incomes'
    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    currency = Column(String, default="NGN")
    date_time = Column(DateTime, default=datetime.now(datetime.timezone.utc))
    description = Column(String)

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    currency = Column(String, default="NGN")
    date_time = Column(DateTime, default=datetime.now(datetime.timezone.utc))
    description = Column(String)
    category_name = Column(String, ForeignKey('categories.name'), nullable=True)
    category = relationship("Category", back_populates="expenses")

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, default="Uncategorized")
    description = Column(String, default="Uncategorized Expenses")
    expenses = relationship("Expense", back_populates="category", cascade="all")
