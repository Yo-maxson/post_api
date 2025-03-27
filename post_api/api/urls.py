from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LetterViewSet, PackageViewSet, TypeofletterViewSet, PackagetypeViewSet

router = DefaultRouter()
router.register(r'letter', LetterViewSet)
router.register(r'package', PackageViewSet)
router.register(r'type_letter', TypeofletterViewSet)
router.register(r'type_package', PackagetypeViewSet)

urlpatterns = [
    path('post/', include(router.urls)),
]
