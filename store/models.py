from django.db import models
from category.models import Category

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    discount_percentage = models.FloatField(default=0.0)
    discount_amount = models.FloatField(default=0.0) 
    images = models.ImageField(upload_to='images/products', blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def calculate_discount(self):
        price_after_percentage = self.price - (self.price * (self.discount_percentage / 100))
        price_after_fixed_discount = self.price - self.discount_amount
        return max(0, min(price_after_percentage, price_after_fixed_discount))

    @property
    def final_price(self):
        return self.calculate_discount()

    def __str__(self):
        return self.product_name
