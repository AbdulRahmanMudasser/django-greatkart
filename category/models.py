from django.db import models

# Category Model
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    category_image = models.ImageField(upload_to='images/categories', blank=True)
    
    def __str__(self):
        return self.category_name
