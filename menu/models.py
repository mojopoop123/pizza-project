from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class MenuItem(models.Model):
    class MenuItemType(models.TextChoices):
        PIZZA = 'PIZZA', _('Pizza')
        DRINK = 'DRINK', _('Drink')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image_url = models.TextField()
    allergens = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    type = models.CharField(choices=MenuItemType.choices, default=MenuItemType.PIZZA, max_length=5)

