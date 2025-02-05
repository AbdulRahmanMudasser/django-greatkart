from django.db import models
from django.urls import reverse
from category.models import Category
from django.utils.text import slugify

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    discount_percentage = models.FloatField(default=0.0, blank=True)
    discounted_price = models.FloatField(default=0.0, blank=True)  # Stores final price after discount
    images = models.ImageField(upload_to='images/products', blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def calculate_discounted_price(self):
        """Calculates the final price after applying the discount percentage."""
        return self.price - (self.price * (self.discount_percentage / 100))

    @property
    def final_price(self):
        """Returns the final price after discount."""
        return self.discounted_price  # This now holds the final discounted price

    def save(self, *args, **kwargs):
        """Automatically update discounted_price and slug before saving."""
        if not self.slug:
            self.slug = slugify(self.product_name)

        # Auto-calculate and store the final discounted price
        self.discounted_price = self.calculate_discounted_price()
        
        super().save(*args, **kwargs)
        
    def get_url(self):
        """Returns the URL for the product details page."""
        return reverse('product_details', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
