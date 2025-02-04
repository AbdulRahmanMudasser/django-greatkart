from django.urls import path
from . import views

urlpatterns = [
    # Store URL
    path('', views.store, name='store'),
    
    # Get Products By Category
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    
    # Product Details Page
    path('<slug:category_slug>/<slug:product_slug>/', views.product_details, name='product_details'),
]
