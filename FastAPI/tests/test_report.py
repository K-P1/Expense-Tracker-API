# tests/test_report.py
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine
from datetime import date

client = TestClient(app)

# Fixture to create a fresh test database
@pytest.fixture(autouse=True)
def create_test_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_report_summary_invalid_dates():
    # Test report summary with an invalid date range
    start_date = "2025-01-10"
    end_date = "2025-01-01"  # Invalid: start_date > end_date
    response = client.get(f"/report/summary?start_date={start_date}&end_date={end_date}")
    assert response.status_code == 400

def test_report_summary_valid():
    # First, create some incomes and expenses
    client.post("/income/", json={"amount": 1000, "description": "Salary"})
    client.post("/expense/", json={"amount": 300, "description": "Groceries", "category_name": "Food"})
    
    # Use today's date for report range
    today = date.today().isoformat()
    response = client.get(f"/report/summary?start_date={today}&end_date={today}")
    assert response.status_code == 200
    data = response.json()
    assert "total_credit" in data
    assert "total_debit" in data

def test_full_report_valid():
    # Create sample records
    today = date.today().isoformat()
    client.post("/category/", json={"name": "Food", "description": "Expenses for food"})
    client.post("/income/", json={"amount": 2000, "description": "Bonus", "date": today})
    client.post("/expense/", json={"amount": 150, "description": "Snacks", "category_name": "Food", "date": today})
    response = client.get(f"/report/full?start_date={today}&end_date={today}")
    print(response.json())

    assert response.status_code == 200
    data = response.json()
    assert "incomes" in data
    assert "expenses" in data
