from django.urls import path, include
from .views import UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

# Include the router's URLs in urlpatterns
urlpatterns = router.urls

