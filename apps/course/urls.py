from rest_framework.routers import DefaultRouter
from apps.course import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'courses', views.CourseViewSet, basename='courses')
router.register(r'exercise', views.ExerciseViewSet, basename='exercise')
router.register(r'exercise_file', views.ExerciseFileViewSet, basename='exercise_file')

# The API URLs are now determined automatically by the router.
urlpatterns = router.urls
