from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, primary_key=True, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Income(models.Model):
    amount = models.IntegerField()
    currency = models.CharField(max_length=10, default="NGN")
    description = models.TextField()
    date = models.DateField(default=timezone.now)
    # Use a lambda to get only the time portion
    time = models.TimeField(default=lambda: timezone.now().time())

    def __str__(self):
        return f"Income {self.id} - {self.amount}"

class Expense(models.Model):
    amount = models.IntegerField()
    currency = models.CharField(max_length=10, default="NGN")
    description = models.TextField()
    date = models.DateField(default=timezone.now)
    # Use a lambda for time as well
    time = models.TimeField(default=lambda: timezone.now().time())
    # ForeignKey to Category
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="expenses")

    def __str__(self):
        return f"Expense {self.id} - {self.amount}"
