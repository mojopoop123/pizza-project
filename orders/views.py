from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from cart.models import CartItem


@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.get_total_price() for item in cart_items)

    if request.method == "POST":
        if not cart_items:
            return redirect("menu")

        order = Order.objects.create(
            user=request.user,
            total_price=total
        )

        for item in cart_items:
            if item.pizza:
                toppings_text = ", ".join(
                    topping.name for topping in item.toppings.all()
                )

                OrderItem.objects.create(
                    order=order,
                    item_name=item.pizza.name,
                    size=item.size.name,
                    toppings=toppings_text,
                    quantity=item.quantity,
                    price=item.get_total_price()
                )

            elif item.drink:
                OrderItem.objects.create(
                    order=order,
                    item_name=item.drink.name,
                    size=item.drink.size,
                    toppings="",
                    quantity=item.quantity,
                    price=item.get_total_price()
                )

        cart_items.delete()

        return redirect("order_confirmation", order_id=order.id)

    return render(request, "orders/checkout.html", {
        "cart_items": cart_items,
        "total": total,
    })

@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    return render(request, "orders/confirmation.html", {"order": order})


@login_required
def order_history(request):
    orders = Order.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(request, "orders/history.html", {"orders": orders})