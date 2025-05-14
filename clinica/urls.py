from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IdentificationViewSet, OwnerViewSet, PetViewSet, AppointmentViewSet

router = DefaultRouter()
router.register(r'identificaciones', IdentificationViewSet)
router.register(r'propietarios', OwnerViewSet)
router.register(r'mascotas', PetViewSet)
router.register(r'citas', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
