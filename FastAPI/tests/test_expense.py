# tests/test_expense.py
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine

client = TestClient(app)



# Fixture to create a fresh test database
@pytest.fixture(autouse=True)
def create_test_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_expense():
    # Test creating a new expense
    payload = {"amount": 500, "description": "Lunch", "category_name": "Food"}
    response = client.post("/expense/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == 500
    assert data["description"] == "Lunch"

def test_get_expense_not_found():
    # Test retrieving an expense that does not exist
    response = client.get("/expense/999")
    assert response.status_code == 404
