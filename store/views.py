from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from cart.models import CartItem
from cart.views import _get_session
from .models import Product
from category.models import Category

# Store View
def store(request, category_slug=None):
    # Get All Available Products & Order Them
    # products = Product.objects.filter(is_available=True)
    products = Product.objects.filter(is_available=True).order_by('id')
    
    # If Category Slug Exists in URL
    if category_slug:
        # Get Category
        category = get_object_or_404(Category, slug=category_slug)
        
        # Get Product By Category
        products = products.filter(category=category)
        
    # Split Products into Pages, Show 6 Per Page
    paginator = Paginator(products, 6)
    
    # Get Current Page from the Request
    page = request.GET.get('page')
    
    # Get Paginated Products for that Page
    paged_products = paginator.get_page(page)
    
    context = {
        # 'products': products,
        'products': paged_products,
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

# Search Product View
def search(request):
    return HttpResponse("Search Page")
