from django.urls import path
from . import views

urlpatterns = [
    # Cart URL
    path('', views.cart, name='cart'),
    
    # Add Cart URL
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    
    # Remove Cart URL
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
    
    # Remove Cart Item URL
    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
]
