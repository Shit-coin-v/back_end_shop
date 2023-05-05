from django.contrib import admin

from mainapp.models import(
    Cart, CartProduct, Product
)

admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Product)