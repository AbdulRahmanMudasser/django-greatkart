from django.http import HttpResponse
from django.shortcuts import render, redirect
from store.models import Product
from .models import Cart, CartItem

# Get Session Key
def _get_session(request):
    # Get Session Key of User
    session_id = request.session.session_key
    
    # Check if Session Key Does Not Exists
    if not session_id:
        # Create  New Session
        session_id = request.session.create()
        
    # Return Session Key
    return session_id

# Add to Cart Function
def add_cart(request, product_id):
    # Get Product By id
    product = Product.objects.get(id=product_id)
    
    try:
        # Find Existing Cart
        cart = Cart.objects.get(cart_id=_get_session(request))
    except Cart.DoesNotExist:
        # Create New Cart
        cart = Cart.objects.create(cart_id=_get_session(request))
        
        # Save Cart
        cart.save()
        
    try:
        # Find Product in Cart
        cart_item = CartItem.objects.get(product=product, cart=cart)
        
        # if Product Exists, Increase Quantity
        cart_item.quantity += 1
        
        # Save Cart Prodcut
        cart_item.save()
    except CartItem.DoesNotExist:
        # if Product does not Exits in Cart, Create Product
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart, is_active=True)
        
        # Save Product
        cart_item.save()
        
    # Check
    # return HttpResponse(cart_item.product)

    # exit()
        
    # Redirect to Cart
    return redirect('cart')
        

# Cart View
def cart(request):
    
    context = {
        
    }
    
    # Render Cart Template
    return render(request, 'cart/cart.html', context)
