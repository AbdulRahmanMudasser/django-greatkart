from django.shortcuts import render

# Register User View
def register_user(request):
    return render(request, 'accounts/register.html')

# Login User View
def login_user(request):
    return render(request, 'accounts/login.html')

# Logout User View
def logout_user(request):
    return 
    # return render(request, 'accounts/logout.html')
