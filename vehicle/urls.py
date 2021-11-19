from django.urls import path, include
from rest_framework.routers import SimpleRouter

from vehicle.views import VehicleViewSet

router = SimpleRouter()

router.register('deer', VehicleViewSet, basename='vehicles')

urlpatterns = [
    path('', include((router.urls)))
]
