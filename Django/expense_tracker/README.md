# Expense Tracker API (Django Version)

This is a Django-based Expense Tracker API built with Django REST Framework. It provides endpoints for managing incomes, expenses, and categories, as well as generating financial reports.

## Features

- **Modular Design:**  
  The project is structured with a dedicated app (`tracker`) that handles models, serializers, views, and URL routing.
- **CRUD Operations:**  
  Endpoints to create, read, update, and delete incomes, expenses, and categories.
- **Reporting:**  
  API endpoints to generate summary and full reports for a specified date range.
- **Validation:**  
  Data is validated using DRF serializers.
- **Logging:**  
  Basic logging is configured in Django's settings.
- **Testing:**  
  Tests for endpoints are written using Django's test framework.

## Project Structure

```
expense_tracker/
├── expense_tracker/           # Django project configuration
│   ├── settings.py            # Project settings (includes DRF and logging configuration)
│   ├── urls.py                # Root URL configuration
│   └── ...
├── tracker/                   # App containing the API logic
│   ├── models.py              # Django models for Income, Expense, and Category
│   ├── serializers.py         # DRF serializers
│   ├── views.py               # API views for CRUD operations and reports
│   ├── urls.py                # App URL routing
│   ├── tests/                 # Test cases for the API endpoints
│   └── ...
├── manage.py
└── README.md
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/expense-tracker-django.git
   cd expense-tracker-django
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

## Usage

1. **Run the Django development server:**
   ```bash
   python manage.py runserver
   ```

2. **API Endpoints:**
   - Incomes: `/api/income/`
   - Expenses: `/api/expense/`
   - Categories: `/api/category/`
   - Report Summary: `/api/report/summary/`
   - Full Report: `/api/report/full/`

3. **Access the API Documentation (if using DRF's browsable API):**
   Open your browser and navigate to `http://127.0.0.1:8000/api/`.

## Testing

Run tests using Django’s test runner:
```bash
python manage.py test
```

## Logging

Logging is configured in `expense_tracker/settings.py` to output to the console. Adjust the configuration as needed.

## Future Improvements

- Add authentication and permissions for secure endpoints.
- Enhance error handling and validation messages.
- Extend reporting functionality.
- Improve test coverage with more scenarios.