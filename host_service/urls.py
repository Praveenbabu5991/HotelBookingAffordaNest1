from django.urls import path
from .views import HotelViewSet, RoomViewSet, BedViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'beds', BedViewSet)

urlpatterns = router.urls
