from sqlalchemy.orm import Session
from sqlalchemy import func
from models import *
from schemas import *

def create_income(db: Session, income: WriteIncome):
    db_income = Income(**income.model_dump())
    db.add(db_income)
    db.commit()
    db.refresh(db_income)
    return db_income

def update_income(db: Session, income_id: int, income: WriteIncome):
    db_income = db.query(Income).filter(Income.id == income_id).first()
    if db_income is None:
        raise ValueError("Income not found")
    for key, value in income.model_dump(exclude_unset=True).items():
        setattr(db_income, key, value)
    db.commit()
    db.refresh(db_income)
    return db_income

def delete_income(db: Session, income_id: int):
    db_income = db.query(Income).filter(Income.id == income_id).first()
    if db_income is None:
        raise ValueError("Income not found")
    db.delete(db_income)
    db.commit()
    return db_income

def get_income(db: Session, income_id: int):
    return db.query(Income).filter(Income.id == income_id).first()

def create_expense(db: Session, expense: WriteExpense):
    db_expense = Expense(**expense.model_dump())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def update_expense(db: Session, expense_id: int, expense: WriteExpense):
    db_expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if db_expense is None:
        raise ValueError("Expense not found")
    for key, value in expense.model_dump(exclude_unset=True).items():
        setattr(db_expense, key, value)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def delete_expense(db: Session, expense_id: int):
    db_expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if db_expense is None:
        raise ValueError("Expense not found")
    db.delete(db_expense)
    db.commit()
    return db_expense

def get_expense(db: Session, expense_id: int):
    return db.query(Expense).filter(Expense.id == expense_id).first()

def create_category(db: Session, category: WriteCategory):
    db_category = Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_category(db: Session, category_id: int, category: WriteCategory):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category is None:
        raise ValueError("Category not found")
    for key, value in category.model_dump(exclude_unset=True).items():
        setattr(db_category, key, value)
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category is None:
        raise ValueError("Category not found")
    db.delete(db_category)
    db.commit()
    return db_category

def calculate_income(db: Session, start_date, end_date):
    total_credit = db.query(func.sum(Income.amount)).filter(
        Income.date_time >= start_date,
        Income.date_time <= end_date
    ).scalar() or 0
    return total_credit

def calculate_expense(db: Session, start_date, end_date):
    total_debit = db.query(func.sum(Expense.amount)).filter(
        Expense.date_time >= start_date,
        Expense.date_time <= end_date
    ).scalar() or 0
    return total_debit

def calculate_balance(db: Session, date):
    total_credit = db.query(func.sum(Income.amount)).filter(
        Income.date_time <= date
    ).scalar() or 0
    total_debit = db.query(func.sum(Expense.amount)).filter(
        Expense.date_time <= date
    ).scalar() or 0
    return total_credit - total_debit

def report_summary(db: Session, report: Report):
    date_range = f"{report.start_date} to {report.end_date}"
    currency = "NGN"
    total_credit = calculate_income(db, report.start_date, report.end_date)
    total_debit = calculate_expense(db, report.start_date, report.end_date)
    start_balance = calculate_balance(db, report.start_date)
    end_balance = start_balance + total_credit - total_debit
    return {
        "date_range": date_range,
        "currency": currency,
        "total_credit": total_credit,
        "total_debit": total_debit,
        "start_balance": start_balance,
        "end_balance": end_balance
    }

    income_instances = db.query(Income.amount).filter(
        Income.date_time <= date
    ).all()
    expense_instances = db.query(Expense.amount).filter(
        Expense.date_time <= date
    ).all()
    total_credit = [income.amount for income in income_instances]
    total_debit = [expense.amount for expense in expense_instances]
    return sum(total_credit) - sum(total_debit)