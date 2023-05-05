from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=127)
    price = models.PositiveIntegerField(default=0)

class Cart(models.Model):
    email = models.EmailField(unique=True)

class CartProduct(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE,
        related_name='card_products'
    )

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='cart_products'
    )

    amount = models.PositiveIntegerField(default=1)
