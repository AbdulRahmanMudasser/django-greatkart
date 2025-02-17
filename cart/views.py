from decimal import Decimal
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from store.models import Product
from .models import Cart, CartItem


# Get Session Key
def _get_session(request):
    # Get Session Key of User
    session_id = request.session.session_key
    
    # Check if Session Key Does Not Exists
    if not session_id:
        # Create New Session
        request.session.create()
        
        # Retrieve Session Key
        session_id = request.session.session_key
        
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

# Remove Cart
def remove_cart(request, product_id):
    # Get Cart by User Session
    cart = Cart.objects.get(cart_id=_get_session(request))
    
    # Get Product
    product = get_object_or_404(Product, id=product_id)

    try:
        # Get Cart Item
        cart_item = CartItem.objects.get(product=product, cart=cart)
        
        if cart_item.quantity > 1:
            # Reduce Quantity
            cart_item.quantity -= 1 
            cart_item.save()
        else:
            # Remove Item if Quantity Reaches 0
            cart_item.delete()

        # Delete Cart if it's Empty
        if not CartItem.objects.filter(cart=cart).exists():
            cart.delete()

    except CartItem.DoesNotExist:
        # Ignore if Item is Not Found
        pass  

    # Redirect to Cart Template
    return redirect('cart')   

# Remove Cart Item
def remove_cart_item(request, product_id):
    # Get Cart by Session
    cart = get_object_or_404(Cart, cart_id=_get_session(request))  
    
    # Get Product
    product = get_object_or_404(Product, id=product_id)

    # Find the Cart Item & Delete if Exists
    cart_item = CartItem.objects.filter(cart=cart, product=product).first()
    
    if cart_item:
        cart_item.delete()

        # Delete Cart if it's Empty
        if not CartItem.objects.filter(cart=cart).exists():
            cart.delete()

    # Redirect to Cart Page
    return redirect('cart')  

# Cart View
def cart(request, total=Decimal('0.00'), quantity=0, cart_items=None):
    try:
        # Get Cart Associated With Current User Session
        cart = Cart.objects.get(cart_id=_get_session(request))

        # Retrieve All Active Cart Items for Cart
        cart_items = CartItem.objects.filter(cart=cart, is_active=True) or []

        # Calculate Total Price & Quantity of Items in Cart
        for cart_item in cart_items:
            total += Decimal(str(cart_item.product.discounted_price)) * cart_item.quantity
            quantity += cart_item.quantity
            
        # Calculating Tax & Grand Total
        tax = (2 * total) / 100
        grand_total = tax + total

    except ObjectDoesNotExist:
        # If Cart or Cart Items Do Not Exist, Ensure cart_items is an Empty List
        cart_items = []

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }

    # Render Cart Template
    return render(request, 'cart/cart.html', context)

