from .models import Category

# Meun Links
def menu_links(request):
    # Get All Categories
    links = Category.objects.all()
    
    # Return links In Form of dictionary
    return dict(links=links)