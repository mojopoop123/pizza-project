from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from menu.models import Pizza, PizzaSize, Topping, Drink
from .models import CartItem


@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.get_total_price() for item in cart_items)

    return render(request, "cart/cart.html", {
        "cart_items": cart_items,
        "total": total,
    })


@login_required
def add_pizza_to_cart(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)

    if request.method == "POST":
        size_id = request.POST.get("size")
        topping_ids = request.POST.getlist("toppings")
        quantity = int(request.POST.get("quantity", 1))

        size = get_object_or_404(PizzaSize, id=size_id)

        cart_item = CartItem.objects.create(
            user=request.user,
            pizza=pizza,
            size=size,
            quantity=quantity,
        )

        cart_item.toppings.set(topping_ids)
        cart_item.save()

    return redirect("menu")


@login_required
def add_drink_to_cart(request, drink_id):
    drink = get_object_or_404(Drink, id=drink_id)

    CartItem.objects.create(
        user=request.user,
        drink=drink,
        quantity=1,
    )

    return redirect("menu")


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()

    return redirect("cart_detail")