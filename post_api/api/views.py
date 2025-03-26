from django.shortcuts import render

from rest_framework import viewsets, status, generics
from django.views.generic import ListView
from .models import *
from .serializers import LeterSerializer, PackageSerializer, TypeofletterSerializer, PackagetypeSerializer


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LeterSerializer


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class TypeofletterViewSet(viewsets.ModelViewSet):
    queryset = Typeofletter.objects.all()
    serializer_class = TypeofletterSerializer


class PackagetypeViewSet(viewsets.ModelViewSet):
    queryset = Packagetype.objects.all()
    serializer_class = PackagetypeSerializer
