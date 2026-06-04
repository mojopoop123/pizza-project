from django.contrib import admin
from .models import Pizza, PizzaSize, Topping, Drink


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ("name", "is_available")
    filter_horizontal = ("available_toppings",)


@admin.register(PizzaSize)
class PizzaSizeAdmin(admin.ModelAdmin):
    list_display = ("name", "base_price", "topping_price")


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ("name", "is_available")


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ("name", "size", "price", "is_available")