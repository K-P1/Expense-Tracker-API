from django.test import TestCase
from django.urls import reverse
from tracker.models import Income
from datetime import date

class IncomeAPITest(TestCase):
    def setUp(self):
        self.today = date.today().isoformat()

    def test_create_income(self):
        url = reverse('income-list')
        payload = {"amount": 1000, "description": "Salary", "date": self.today}
        response = self.client.post(url, payload, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data['amount'], 1000)
        self.assertEqual(data['description'], "Salary")

    def test_get_income(self):
        income = Income.objects.create(amount=1000, description="Salary", date=self.today)
        url = reverse('income-detail', args=[income.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['amount'], 1000)
        self.assertEqual(data['description'], "Salary")
