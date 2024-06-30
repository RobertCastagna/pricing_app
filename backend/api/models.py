from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    # class Meta:
    #     app_label = 'prods'
    name = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PriceHistory(models.Model):
    # class Meta:
    #     app_label = 'prices'
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.product.name} - {self.price} on {self.date}"

class Budget(models.Model):
    # class Meta:
    #     app_label = 'budgets'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_expenses = models.DecimalField(max_digits=10, decimal_places=2)
    savings_goal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username}'s Budget"
