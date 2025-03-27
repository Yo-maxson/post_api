from django.test import TestCase
from .serializers import LeterSerializer, PackageSerializer, TypeofletterSerializer, PackagetypeSerializer
from rest_framework.test import APIClient
from rest_framework import status
from .models import *


class LetterSerializerTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.url = '/api/v1/post/letter/'
        self.typeofletter_data = {"name": "письмо"}
        self.typeofletter = Typeofletter.objects.create(**self.typeofletter_data)

        self.letter_data = {
            "sender": "Иванов Иван Иваныч",
            "recipient": "Иванова Иванка Ивановна",
            "sending": "Город А",
            "receiving": "Город Б",
            "senders_index": 12345,
            "recipients_index": 543210,
            "letter_weight": 1.2,
            "type_of_letter": self.typeofletter
        }
        self.letter_data_create = {
            "sender": "Иванова Ивана Иваныча",
            "recipient": "Иванова Иванка Ивановна",
            "sending": "Город Б",
            "receiving": "Город В",
            "senders_index": 1234,
            "recipients_index": 543210,
            "letter_weight": 1.2,
            "type_of_letter": 3
        }
        self.letter = Letter.objects.create(**self.letter_data)

        self.serializer = LeterSerializer(instance=self.letter)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()),
                         {'id', 'sender', 'recipient', 'sending', 'receiving', 'senders_index', 'recipients_index',
                          'type_of_letter', 'letter_weight'})

    def test_sender_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['sender'], self.letter_data['sender'])

    def test_get_letter(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_post_letter(self):
        response = self.client.post(self.url, self.letter_data_create, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Letter.objects.count(), 2)


class PackageSerializerTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.packagetype_data = {"name": "посылкка"}
        self.packagetype = Packagetype.objects.create(**self.packagetype_data)

        self.package_data_get = {
            "sender": "Иванов Иван Иваныч",
            "recipient": "Иванова Иванка Ивановна",
            "sending": "Город А",
            "receiving": "Город Б",
            "senders_index": 12345,
            "recipients_index": 543210,
            "package_weight": 1.2,
            "package_type": self.packagetype
        }
        self.package_data_post = {
            "sender": "Иванов Иван Иваныч",
            "recipient": "Иванова Иванка Ивановна",
            "sending": "Город А",
            "receiving": "Город В",
            "senders_index": 12345,
            "recipients_index": 543210,
            "package_weight": 1.2,
            "package_type": 1
        }
        self.package = Package.objects.create(**self.package_data_get)
        self.serializer = PackageSerializer(instance=self.package)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()),
                         {'id', 'sender', 'recipient', 'sending', 'receiving', 'senders_index', 'recipients_index',
                          'package_type', 'package_weight'})

    def test_get_package(self):
        url = '/api/v1/post/package/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_post_package(self):
        url = '/api/v1/post/letter/'
        response = self.client.post(url, self.package_data_post, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Package.objects.count(), 1)


class TypeletterSerializerTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/v1/post/type_letter/'
        self.type_letter_data = {"name": "письмо"}

        self.type_letter = Typeofletter.objects.create(**self.type_letter_data)
        self.serializer = TypeofletterSerializer(instance=self.type_letter)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()),
                         {'id', 'name'})

    def test_get_package(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class PackagetypeSerializerTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/v1/post/type_package/'
        self.package_type_data = {"name": "посылкка"}

        self.package_type = Packagetype.objects.create(**self.package_type_data)
        self.serializer = PackagetypeSerializer(instance=self.package_type)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()),
                         {'id', 'name'})

    def test_get_package(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
