from django.db import models


class PizzaSize(models.Model):
    name = models.CharField(max_length=50)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    topping_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    available_toppings = models.ManyToManyField(Topping, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.size})"