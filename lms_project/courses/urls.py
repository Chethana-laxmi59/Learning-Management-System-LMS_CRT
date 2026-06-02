from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonViewSet, CategoryViewSet

router = DefaultRouter()
router.register('courses', CourseViewSet)
router.register('lessons', LessonViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [path('', include(router.urls))]
