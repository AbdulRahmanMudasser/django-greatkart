from django.shortcuts import render, redirect
from store.models import Product
from .models import Cart, CartItem

# Get Session Key
def _get_session(request):
    # Get Session Key
    session_id = request.session.session_key
    
    # Check if Session is not Created yet
    if not session_id:
        # Create a New Session
        session_id = request.session.create()
        
    # Return Session Id
    return session_id

# Add to Cart Function
def cart_view(request, product_id):
    # Get Product By id
    product = Product.objects.get(id=product_id)
    
    try:
        cart = Cart.objects.get(cart_id=_get_session(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_get_session(request))
        
        cart.save()
        
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cart_item.save()
        
    return redirect()
        

# Cart View
def cart(request):
    
    context = {
        
    }
    
    # Render Cart Template
    return render(request, 'cart/cart.html', context)
