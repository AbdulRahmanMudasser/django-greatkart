from django.shortcuts import render
from store.models import Product

# Home View
def home(request):
    # Filter Products
    products = Product.objects.all().filter(is_available=True)
    
    context = {
        'products': products,
    }
    
    return render(request, 'home.html', context) 
