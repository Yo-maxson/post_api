from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Letter, Package, Typeofletter, Packagetype
from .serializers import LeterSerializer, PackageSerializer, TypeofletterSerializer, PackagetypeSerializer


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LeterSerializer

    def create(self, request, *args, **kwargs):
        request.data['senders_index'] = '0' * (6 - len(str(request.data['senders_index']))) + str(
            request.data['senders_index'])

        request.data['recipients_index'] = '0' * (6 - len(str(request.data['recipients_index']))) + str(
            request.data['recipients_index'])

        serializer = self.serializer_class(data=request.data, )  # or request.data

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

    def create(self, request, *args, **kwargs):
        request.data['senders_index'] = '0' * (6 - len(str(request.data['senders_index']))) + str(
            request.data['senders_index'])

        request.data['recipients_index'] = '0' * (6 - len(str(request.data['recipients_index']))) + str(
            request.data['recipients_index'])

        serializer = self.serializer_class(data=request.data, )  # or request.data
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TypeofletterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Typeofletter.objects.all()
    serializer_class = TypeofletterSerializer


class PackagetypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Packagetype.objects.all()
    serializer_class = PackagetypeSerializer
