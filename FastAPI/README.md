# Financial API

A modular FastAPI application for managing financial transactions (incomes, expenses, and categories) and generating financial reports. This project demonstrates best practices for code organization, CRUD operations with SQLAlchemy, Pydantic schemas, logging, and testing.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Logging](#logging)
- [Future Improvements](#future-improvements)

## Features

- **Modular Design:**  
  Clear separation of concerns using routers, CRUD classes, and utility modules.
- **CRUD Operations:**  
  Create, read, update, and delete endpoints for incomes, expenses, and categories.
- **Reporting:**  
  Generate summary and full reports for a given date range.
- **Validation:**  
  Pydantic schemas validate and serialize incoming/outgoing data.
- **Logging:**  
  Basic logging for tracking operations and debugging.
- **Testing:**  
  Test cases for all endpoints using FastAPI’s TestClient and pytest.

## Project Structure

```
FastAPI/
├── app/
│   ├── __init__.py
│   ├── main.py              # Entry point for the FastAPI app
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── database.py          # Database configuration (SQLite)
│   ├── crud.py              # CRUD operations encapsulated in classes
│   ├── routers/             # API route definitions split by resource
│   │   ├── __init__.py
│   │   ├── income.py
│   │   ├── expense.py
│   │   ├── category.py
│   │   └── report.py
│   └── utils/
│       ├── __init__.py
│       └── logger.py      # Logging configuration
├── tests/
│   ├── __init__.py
│   ├── test_income.py
│   ├── test_expense.py
│   ├── test_category.py
│   └── test_report.py
├── requirements.txt
└── README.md
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/K-P1/Expense-Tracker-API.git
   cd financial-api
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations (if using Alembic or similar) or let the app create the SQLite DB automatically.**

## Usage

1. **Start the FastAPI server:**
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the API documentation:**
   Open your browser and navigate to [http://localhost:8000/docs](http://localhost:8000/docs).

## API Endpoints

- **Income Endpoints:** `/income/`
  - `POST /income/` – Create a new income record.
  - `GET /income/{income_id}` – Retrieve an income by ID.
  - `PUT /income/{income_id}` – Update an income record.
  - `DELETE /income/{income_id}` – Delete an income record.

- **Expense Endpoints:** `/expense/`
  - `POST /expense/` – Create a new expense record.
  - `GET /expense/{expense_id}` – Retrieve an expense by ID.
  - `PUT /expense/{expense_id}` – Update an expense record.
  - `DELETE /expense/{expense_id}` – Delete an expense record.

- **Category Endpoints:** `/category/`
  - `POST /category/` – Create a new category.
  - `GET /category/{category_name}` – Retrieve a category by name.
  - `PUT /category/{category_name}` – Update a category.
  - `DELETE /category/{category_name}` – Delete a category.

- **Report Endpoints:** `/report/`
  - `GET /report/summary` – Generate a summary report for a given date range.
  - `GET /report/full` – Generate a full report (including incomes and expenses) for a given date range.

## Testing

Tests are written using [pytest](https://pytest.org/) and FastAPI’s TestClient.

1. **Run tests:**
   ```bash
   pytest
   ```

   Tests are located in the `tests/` folder and cover endpoints for income, expense, category, and report functionalities.

## Logging

- Logging is configured in `app/utils/logger.py`.
- The logging format includes timestamps, log levels, and messages.
- CRUD operations and endpoints log key events like record creation, updates, deletions, and error conditions.

## Future Improvements

- **Database Migrations:** Integrate Alembic for managing schema changes.
- **Enhanced Error Handling:** Improve exception management and provide more detailed error responses.
- **Authentication & Authorization:** Secure endpoints with authentication mechanisms.
- **Asynchronous Support:** Explore asynchronous database operations for scalability.
- **Additional Tests:** Increase test coverage and add integration tests.

---