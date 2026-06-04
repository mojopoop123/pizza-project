from django.db import models
from django.contrib.auth.models import User
from menu.models import Pizza, PizzaSize, Topping, Drink


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.SET_NULL, null=True, blank=True)
    drink = models.ForeignKey(Drink, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.ForeignKey(PizzaSize, on_delete=models.SET_NULL, null=True, blank=True)
    toppings = models.ManyToManyField(Topping, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        if self.pizza and self.size:
            topping_total = self.toppings.count() * self.size.topping_price
            return (self.size.base_price + topping_total) * self.quantity

        if self.drink:
            return self.drink.price * self.quantity

        return 0

    def __str__(self):
        if self.pizza:
            return f"{self.quantity}x {self.pizza.name}"
        return f"{self.quantity}x {self.drink.name}"