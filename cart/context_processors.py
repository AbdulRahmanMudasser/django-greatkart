from cart.models import Cart, CartItem
from cart.views import _get_session
from django.db.models import Sum

# def cart_counter(request):
#     cart_count = 0
    
#     if 'admin' in request.path:
#         return {}
    
#     else:
#         try:
#             # Get Current Cart By User Session
#             cart = Cart.objects.filter(cart_id=_get_session(request))
            
#             cart_items = CartItem.objects.all().filter(cart=cart[:1])
            
#             for cart_item in cart_items:
#                 cart_count += cart_item.quantity
                
#         except Cart.DoesNotExist:
#             cart_count = 0
            
#     return dict(cart_count=cart_count)

# Cart Counter
def cart_counter(request):
    # If Admin, We Don't Need to Check their Cart
    if 'admin' in request.path:
        return {}
    
    # Get User Session
    user_session = _get_session(request)
    
    # Get Cart of User by Session
    cart = Cart.objects.filter(cart_id=user_session).first()
    
    cart_count = 0
        
    if cart:
        cart_count = CartItem.objects.filter(cart=cart).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        
    return dict(cart_count=cart_count)    
    