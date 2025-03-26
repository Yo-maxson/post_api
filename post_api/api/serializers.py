from rest_framework import serializers
from .models import *

class LeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = '__all__'


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

