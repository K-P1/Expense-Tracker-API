# tests/test_category.py
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

def test_create_category():
    # Test creating a new category
    payload = {"name": "Food", "description": "Expenses for food"}
    response = client.post("/category/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Food"
    assert data["description"] == "Expenses for food"

def test_get_category_not_found():
    # Test retrieving a category that does not exist
    response = client.get("/category/NonExistent")
    assert response.status_code == 404
