from decimal import Decimal
from django.db import models
from django.urls import reverse
from store.models import Product

# Cart Model
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
    
    def __str__(self):
        return self.cart_id
    
# Cart Item Model
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"

    def __str__(self):
        return f"{self.product.product_name} ({self.quantity})" 

    def sub_total(self):
        return Decimal(str(self.product.discounted_price)) * self.quantity 
