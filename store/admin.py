from django.contrib import admin
from .models import Product

# Product Admin Class
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'price', 'discounted_price', 'stock', 'category', 'modified_date', 'is_available')
    
# Register Product & Product Admin
admin.site.register(Product, ProductAdmin)
