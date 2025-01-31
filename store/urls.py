from django.urls import path
from . import views

urlpatterns = [
    # Store URL
    path('', views.store, name='store'),
    
    # Get Products By Category
    path('<slug:category_slug>/', views.store, name='products_by_category'),
]
