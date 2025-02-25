from django.test import TestCase
from django.urls import reverse
from tracker.models import Expense, Category
from datetime import date

class ExpenseAPITest(TestCase):
    def setUp(self):
        self.today = date.today().isoformat()
        self.category = Category.objects.create(name="Food", description="Food Expenses")

    def test_create_expense(self):
        url = reverse('expense-list')
        payload = {
            "amount": 500,
            "description": "Lunch",
            "date": self.today,
            "category": "Food"  # Using the category name for writing
        }
        response = self.client.post(url, payload, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data['amount'], 500)
        self.assertEqual(data['description'], "Lunch")
        # For read operations, the output should include category_name:
        self.assertEqual(data.get('category_name'), "Food")

    def test_get_expense(self):
        expense = Expense.objects.create(
            amount=500,
            description="Lunch",
            date=self.today,
            category=self.category
        )
        url = reverse('expense-detail', args=[expense.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['amount'], 500)
        self.assertEqual(data['description'], "Lunch")
        self.assertEqual(data.get('category_name'), "Food")
