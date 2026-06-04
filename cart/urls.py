from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart_detail, name="cart_detail"),
    path("add-pizza/<int:pizza_id>/", views.add_pizza_to_cart, name="add_pizza_to_cart"),
    path("add-drink/<int:drink_id>/", views.add_drink_to_cart, name="add_drink_to_cart"),
    path("remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
]