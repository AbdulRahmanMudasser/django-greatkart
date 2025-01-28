from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    # Fields to Display
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    
    # Links 
    list_display_links = ('email', 'first_name', 'last_name')
    
    # Readonly Fields
    readonly_fields = ('last_login', 'date_joined')
    
    # In Descending Order
    ordering = ('-date_joined',)
    
    # Because We Are Using Custom User Model
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register Account Model
admin.site.register(Account, AccountAdmin)
