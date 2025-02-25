# app/routers/report.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import date
from app.schemas import Report, ReadSummary, ReadReport
from app.database import SessionLocal
from app.crud import CRUDReport

router = APIRouter()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/summary", response_model=ReadSummary)
async def get_report_summary(
    start_date: date = Query(..., title="Start Date", description="The start date for the report"),
    end_date: date = Query(..., title="End Date", description="The end date for the report"),
    db: Session = Depends(get_db)
):
    report = Report(start_date=start_date, end_date=end_date)
    try:
        return CRUDReport.report_summary(db, report)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/full", response_model=ReadReport)
async def get_full_report(
    start_date: date = Query(..., title="Start Date", description="The start date for the report"),
    end_date: date = Query(..., title="End Date", description="The end date for the report"),
    db: Session = Depends(get_db)
):
    report = Report(start_date=start_date, end_date=end_date)
    try:
        return CRUDReport.full_report(db, report)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
