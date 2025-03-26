from django.shortcuts import render

from rest_framework import viewsets, status

from .models import *
from .serializers import LeterSerializer, PackageSerializer


class LetterViewSet(viewsets.ViewSet):
    queryset = Letter.objects.all()
    serializer = LeterSerializer


class PackageViewSet(viewsets.ViewSet):
    queryset = Package.objects.all()
    serializer = PackageSerializer

