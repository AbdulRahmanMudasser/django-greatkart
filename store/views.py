from django.shortcuts import render, get_object_or_404

from cart.models import CartItem
from cart.views import _get_session
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
def product_details(request, category_slug=None, product_slug=None):
    try:
        # Try to Get Product By Category
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        
        # Checking if Item is in Cart
        in_cart = CartItem.objects.filter(cart__cart_id=_get_session(request), product=single_product).exists()
        
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    
    # Render Product Details Template
    return render(request, 'store/product_details.html', context)
