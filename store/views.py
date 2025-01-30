from django.shortcuts import render
from .models import Product

# Store View
def store(request):
    # Get All Products
    products = Product.objects.all().filter(is_available=True)
    
    # Get Products Count
    products_count = products.count()
    
    context = {
        'products': products,
        'products_count': products_count,
    }
    
    return render(request, 'store/store.html', context)
