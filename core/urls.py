from django.urls import include, path
from rest_framework import routers
from .views import ClienteViewSet, CuentaViewSet, MovimientoViewSet

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet)
router.register('cuentas', CuentaViewSet)
router.register('movimientos', MovimientoViewSet)

urlpatterns = router.urls
