from django.shortcuts import render

# Cart View
def cart(request):
    
    context = {
        
    }
    
    # Render Cart Template
    return render(request, 'cart/cart.html', context)
