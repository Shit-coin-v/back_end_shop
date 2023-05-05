from rest_framework.routers import DefaultRouter as DR

from mainapp.views import(
    CartView
)

router = DR()

router.register('cart', CartView)

urlpatterns = []

urlpatterns += router.urls