from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Home URL
    path('', views.home, name='home'),
    
    # Store URL
    path('store/', include('store.urls')),
    
    # Cart URL
    path('cart/', include('cart.urls')),
    
    # Accounts URL
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
