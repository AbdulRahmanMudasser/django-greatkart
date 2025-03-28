from django import forms
from .models import Account

# Register User Form
class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']