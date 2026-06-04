from django.shortcuts import render
from .models import Pizza, PizzaSize, Drink


def menu_list(request):

    pizzas = Pizza.objects.filter(is_available=True)

    sizes = PizzaSize.objects.all()

    drinks = Drink.objects.filter(is_available=True)

    return render(
        request,
        "menu/menu.html",
        {
            "pizzas": pizzas,
            "sizes": sizes,
            "drinks": drinks,
        }
    )