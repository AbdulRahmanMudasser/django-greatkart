from django.shortcuts import render

from accounts.forms import RegisterUserForm
from accounts.models import Account, AccountManager

# Register User View
def register_user(request):
    # Check if Request Method is POST
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        
        # Check if form is Valid
        if form.is_valid():
            # Grab Required Things to Create User
            first_name, last_name, phone_number, email, password = (
                form.cleaned_data['first_name'],
                form.cleaned_data['last_name'],
                form.cleaned_data['phone_number'],
                form.cleaned_data['email'],
                form.cleaned_data['password']
            )
            
            username = email.split("@")[0]
            
            # Create User
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            
            user.phone_number = phone_number
            
            # Save User
            user.save()
            
    # if Request if GET
    else:
       form = RegisterUserForm() 
    
    context = {
        'form': form,
    }
    
    return render(request, 'accounts/register.html', context)

# Login User View
def login_user(request):
    return render(request, 'accounts/login.html')

# Logout User View
def logout_user(request):
    return 
    # return render(request, 'accounts/logout.html')
