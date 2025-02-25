from django.test import TestCase
from django.urls import reverse
from tracker.models import Category

class CategoryAPITest(TestCase):
    def test_create_category(self):
        url = reverse('category-list')
        payload = {"name": "Food", "description": "Expenses for food"}
        response = self.client.post(url, payload, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data['name'], "Food")
        self.assertEqual(data['description'], "Expenses for food")

    def test_get_category(self):
        category = Category.objects.create(name="Food", description="Expenses for food")
        url = reverse('category-detail', args=[category.name])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['name'], "Food")
        self.assertEqual(data['description'], "Expenses for food")
