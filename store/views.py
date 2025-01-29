from django.shortcuts import render

# Store View
def store(request):
    return render(request, 'store/store.html')
