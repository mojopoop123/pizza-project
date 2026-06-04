from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order


@login_required
def checkout(request):
    if request.method == "POST":
        order = Order.objects.create(
            user=request.user,
            total_price=0
        )

        return redirect("order_confirmation", order_id=order.id)

    return render(request, "orders/checkout.html")


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