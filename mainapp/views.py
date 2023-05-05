from rest_framework.viewsets import ModelViewSet

from mainapp.models import(
    Product, CartProduct, Cart
)

from mainapp.serializers import(
    CartSerializer,
)

class CartView(ModelViewSet):
    queryset = Cart.objects.all()                   
    serializer_class = CartSerializer


