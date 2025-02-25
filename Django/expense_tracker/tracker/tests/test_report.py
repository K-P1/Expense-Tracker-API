from django.test import TestCase
from django.urls import reverse
from tracker.models import Income, Expense, Category
from datetime import date
import json

class ReportAPITest(TestCase):
    def setUp(self):
        # Create a category for expenses
        self.category = Category.objects.create(name="Food", description="Expenses for food")
        self.today = date.today()

        # Create sample income and expense records with today's date
        Income.objects.create(amount=2000, description="Bonus", date=self.today)
        Expense.objects.create(amount=150, description="Snacks", category=self.category, date=self.today)

    def test_full_report_valid(self):
        url = reverse('full-report')  # Matches our URL name in tracker/urls.py
        response = self.client.get(url, {'start_date': self.today.isoformat(), 'end_date': self.today.isoformat()})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('incomes', data)
        self.assertIn('expenses', data)

    def test_report_summary_invalid_dates(self):
        url = reverse('report-summary')
        response = self.client.get(url, {'start_date': '2025-01-10', 'end_date': '2025-01-01'})
        self.assertEqual(response.status_code, 400)
