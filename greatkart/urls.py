from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Home URL
    path('', views.home, name='home'),
]
