from django.contrib import admin
from .models import Cart, CartItem

# Register Cart, CartItem Model
admin.site.register(Cart)
admin.site.register(CartItem)
