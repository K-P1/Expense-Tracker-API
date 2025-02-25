# tests/test_income.py
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal

client = TestClient(app)

# Create a fresh test database for testing
@pytest.fixture(autouse=True)
def create_test_db():
    # Recreate tables before each test session
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_income():
    # Test creating a new income
    payload = {"amount": 1000, "description": "Salary"}
    response = client.post("/income/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == 1000
    assert data["description"] == "Salary"

def test_get_income_not_found():
    # Test retrieving an income that does not exist
    response = client.get("/income/999")
    assert response.status_code == 404
