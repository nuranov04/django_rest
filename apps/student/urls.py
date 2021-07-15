from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')


urlpatterns = router.urls