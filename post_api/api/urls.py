from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LetterViewSet, PackageViewSet

router = DefaultRouter()
router.register(r'letter', LetterViewSet)
router.register(r'package', PackageViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
