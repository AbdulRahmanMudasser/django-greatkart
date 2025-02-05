from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

# Store View
def store(request, category_slug=None):
    # Get All Available Products
    products = Product.objects.filter(is_available=True)
    
    # If Category Slug Exists in URL
    if category_slug:
        # Get Category
        category = get_object_or_404(Category, slug=category_slug)
        
        # Get Product By Category
        products = products.filter(category=category)
    
    context = {
        'products': products,
        'products_count': len(products),
    }

    # Render Store Template
    return render(request, 'store/store.html', context)

# Product Details View
def product_details(request, category_slug, product_slug):
    try:
        # Try to Get Product By Category
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
    }
    
    # Render Product Details Template
    return render(request, 'store/product_details.html', context)
