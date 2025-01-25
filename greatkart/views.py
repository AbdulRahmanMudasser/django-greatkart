from django.shortcuts import render

# Home View
def home(request):
    return render(request, 'home.html')