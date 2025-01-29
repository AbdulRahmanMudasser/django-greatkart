from django.urls import path
from . import views

urlpatterns = [
    # Store URL
    path('', views.store, name='store'),
]
