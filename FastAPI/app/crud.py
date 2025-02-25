# app/crud.py
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import Income, Expense, Category
from app.schemas import WriteIncome, WriteExpense, WriteCategory, Report, ReadIncome, ReadExpense, ReadReport, ReadSummary
from app.utils.logger import logger

# CRUD operations for Income
class CRUDIncome:
    @staticmethod
    def create(db: Session, income: WriteIncome):
        db_income = Income(**income.model_dump(exclude_unset=True))
        db.add(db_income)
        db.commit()
        db.refresh(db_income)
        logger.info("Created income with id %s", db_income.id)
        return db_income

    @staticmethod
    def update(db: Session, income_id: int, income: WriteIncome):
        db_income = db.query(Income).filter(Income.id == income_id).first()
        if db_income is None:
            logger.error("Income not found for id %s", income_id)
            raise ValueError("Income not found")
        for key, value in income.model_dump(exclude_unset=True).items():
            setattr(db_income, key, value)
        db.commit()
        db.refresh(db_income)
        logger.info("Updated income with id %s", income_id)
        return db_income

    @staticmethod
    def delete(db: Session, income_id: int):
        db_income = db.query(Income).filter(Income.id == income_id).first()
        if db_income is None:
            logger.error("Income not found for deletion with id %s", income_id)
            raise ValueError("Income not found")
        db.delete(db_income)
        db.commit()
        logger.info("Deleted income with id %s", income_id)
        return db_income

    @staticmethod
    def get(db: Session, income_id: int):
        return db.query(Income).filter(Income.id == income_id).first()

    @staticmethod
    def get_all(db: Session):
        return db.query(Income).all()


# CRUD operations for Expense
class CRUDEexpense:
    @staticmethod
    def create(db: Session, expense: WriteExpense):
        db_expense = Expense(**expense.model_dump(exclude_unset=True))
        db.add(db_expense)
        db.commit()
        db.refresh(db_expense)
        logger.info("Created expense with id %s", db_expense.id)
        return db_expense

    @staticmethod
    def update(db: Session, expense_id: int, expense: WriteExpense):
        db_expense = db.query(Expense).filter(Expense.id == expense_id).first()
        if db_expense is None:
            logger.error("Expense not found for id %s", expense_id)
            raise ValueError("Expense not found")
        for key, value in expense.model_dump(exclude_unset=True).items():
            setattr(db_expense, key, value)
        db.commit()
        db.refresh(db_expense)
        logger.info("Updated expense with id %s", expense_id)
        return db_expense

    @staticmethod
    def delete(db: Session, expense_id: int):
        db_expense = db.query(Expense).filter(Expense.id == expense_id).first()
        if db_expense is None:
            logger.error("Expense not found for deletion with id %s", expense_id)
            raise ValueError("Expense not found")
        db.delete(db_expense)
        db.commit()
        logger.info("Deleted expense with id %s", expense_id)
        return db_expense

    @staticmethod
    def get(db: Session, expense_id: int):
        return db.query(Expense).filter(Expense.id == expense_id).first()

    @staticmethod
    def get_all(db: Session):
        return db.query(Expense).all()


# CRUD operations for Category
class CRUDCategory:
    @staticmethod
    def create(db: Session, category: WriteCategory):
        db_category = Category(**category.model_dump(exclude_unset=True))
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        logger.info("Created category with name %s", db_category.name)
        return db_category

    @staticmethod
    def update(db: Session, category_name: str, category: WriteCategory):
        db_category = db.query(Category).filter(Category.name == category_name).first()
        if db_category is None:
            logger.error("Category not found for name %s", category_name)
            raise ValueError("Category not found")
        for key, value in category.model_dump(exclude_unset=True).items():
            setattr(db_category, key, value)
        db.commit()
        db.refresh(db_category)
        logger.info("Updated category with name %s", category_name)
        return db_category

    @staticmethod
    def delete(db: Session, category_name: str):
        db_category = db.query(Category).filter(Category.name == category_name).first()
        if db_category is None:
            logger.error("Category not found for deletion with name %s", category_name)
            raise ValueError("Category not found")
        db.delete(db_category)
        db.commit()
        logger.info("Deleted category with name %s", category_name)
        return db_category

    @staticmethod
    def get(db: Session, category_name: str):
        return db.query(Category).filter(Category.name == category_name).first()

    @staticmethod
    def get_all(db: Session):
        return db.query(Category).all()


# Report related functions
class CRUDReport:
    @staticmethod
    def calculate_income(db: Session, start_date, end_date):
        total_credit = db.query(func.sum(Income.amount)).filter(
            Income.date >= start_date,
            Income.date <= end_date
        ).scalar() or 0
        return total_credit

    @staticmethod
    def calculate_expense(db: Session, start_date, end_date):
        total_debit = db.query(func.sum(Expense.amount)).filter(
            Expense.date >= start_date,
            Expense.date <= end_date
        ).scalar() or 0
        return total_debit

    @staticmethod
    def calculate_balance(db: Session, date):
        total_credit = db.query(func.sum(Income.amount)).filter(
            Income.date <= date
        ).scalar() or 0
        total_debit = db.query(func.sum(Expense.amount)).filter(
            Expense.date <= date
        ).scalar() or 0
        balance = total_credit - total_debit
        return balance

    @staticmethod
    def validate_report_dates(report: Report):
        # Raise error if the start date is after the end date
        if report.start_date > report.end_date:
            logger.error("Invalid report date range: %s to %s", report.start_date, report.end_date)
            raise ValueError("Start date cannot be greater than end date")
        return True

    @staticmethod
    def report_summary(db: Session, report: Report):
        CRUDReport.validate_report_dates(report)
        date_range = f"{report.start_date} to {report.end_date}"
        currency = "NGN"
        total_credit = CRUDReport.calculate_income(db, report.start_date, report.end_date)
        total_debit = CRUDReport.calculate_expense(db, report.start_date, report.end_date)
        total_income = db.query(Income).count()
        total_expense = db.query(Expense).count()
        start_balance = CRUDReport.calculate_balance(db, report.start_date)
        end_balance = start_balance + total_credit - total_debit
        logger.info("Generated summary report for range %s", date_range)
        return ReadSummary(
            date_range=date_range,
            currency=currency,
            total_credit=total_credit,
            total_debit=total_debit,
            total_income=total_income,
            total_expense=total_expense,
            start_balance=start_balance,
            end_balance=end_balance
        )

    @staticmethod
    def full_report(db: Session, report: Report):
        CRUDReport.validate_report_dates(report)
        date_range = f"{report.start_date} to {report.end_date}"
        currency = "NGN"
        total_credit = CRUDReport.calculate_income(db, report.start_date, report.end_date)
        total_debit = CRUDReport.calculate_expense(db, report.start_date, report.end_date)
        start_balance = CRUDReport.calculate_balance(db, report.start_date)
        end_balance = start_balance + total_credit - total_debit        
        total_income = db.query(Income).count()
        total_expense = db.query(Expense).count()
        incomes = db.query(Income).filter(Income.date >= report.start_date, Income.date <= report.end_date).all()
        expenses = db.query(Expense).filter(Expense.date >= report.start_date, Expense.date <= report.end_date).all()
        logger.info("Generated full report for range %s", date_range)
        return ReadReport(
            date_range=date_range,
            currency=currency,
            total_credit=total_credit,
            total_debit=total_debit,
            total_income=total_income,
            total_expense=total_expense,
            start_balance=start_balance,
            end_balance=end_balance,
            incomes = [ReadIncome.model_validate(vars(income)) for income in incomes],
            expenses = [ReadExpense.model_validate(vars(expense)) for expense in expenses]
        )