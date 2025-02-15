from django.urls import path
from . import views

urlpatterns = [
    # Cart URL
    path('', views.cart, name='cart'),
    
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
]
