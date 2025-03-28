from rest_framework import serializers
from .models import Letter, Package, Typeofletter, Packagetype


class LeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = '__all__'


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


class TypeofletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Typeofletter
        fields = '__all__'


class PackagetypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packagetype
        fields = '__all__'
