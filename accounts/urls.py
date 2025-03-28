from django.urls import path
from . import views

urlpatterns = [
    # Register User URL
    path('register/', views.register_user, name='register'),
    
    # Login User URL
    path('login/', views.login_user, name='login'),
        
    # Logout User URL
    path('logout/', views.logout_user, name='logout'),
]
