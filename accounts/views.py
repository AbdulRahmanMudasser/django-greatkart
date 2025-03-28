from django.shortcuts import render

from accounts.forms import RegisterUserForm

# Register User View
def register_user(request):
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
