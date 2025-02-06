from django.urls import path
from . import views

urlpatterns = [
    # Cart URL
    path('', views.cart, name='cart'),
]
