# Expense Tracker API

This repository contains two separate implementations of an Expense Tracker API:

- **Django Version:** A fully featured REST API built using Django and Django REST Framework.
- **FastAPI Version:** A high-performance API built using FastAPI and Pydantic.

Both implementations provide similar functionality:
- Managing incomes, expenses, and categories.
- Generating financial reports (both summary and detailed).
- Well-organized code structure with modular design, logging, and tests.

## Project Structure

```
Expense Tracker API/
├── Django/
│   ├── expense_tracker/        # Django project files and settings
│   ├── tracker/                # Django app (models, views, serializers, tests, etc.)
│   └── README.md               # Detailed instructions for the Django implementation
├── FastAPI/
│   ├── app/                    # FastAPI application code (routers, models, schemas, crud, etc.)
│   ├── tests/                  # Tests for FastAPI endpoints
│   └── README.md               # Detailed instructions for the FastAPI implementation
└── README.md                   # This file – an overview of the entire project
```

## Quick Overview

- **Django Implementation:**  
  The Django version leverages Django REST Framework to provide a robust, scalable API with a traditional MVC structure. It includes detailed documentation on setup, usage, and testing in its own README.

- **FastAPI Implementation:**  
  The FastAPI version focuses on high performance and simplicity using asynchronous endpoints and Pydantic for data validation. Its README contains specific instructions on installation, running, and testing.

## Getting Started

For detailed instructions on setting up, running, and testing each version, please refer to the README files in the respective subfolders:

- **Django Version:**  
  Navigate to the `Django/` folder and open the [README.md](Django/README.md) file.

- **FastAPI Version:**  
  Navigate to the `FastAPI/` folder and open the [README.md](FastAPI/README.md) file.

## Contributing

Contributions, suggestions, and improvements are welcome! Please create an issue or submit a pull request with your changes.