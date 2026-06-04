from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='menu_images')
    allergens = models.CharField(max_length=200)
    active = models.BooleanField(default=True)