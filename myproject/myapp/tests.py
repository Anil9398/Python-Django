from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Shop

class ShopTests(APITestCase):
    def setUp(self):
        # Create some test shops
        Shop.objects.create(name='Shop A', address='Address A', latitude=40.7589, longitude=-73.9851)
        Shop.objects.create(name='Shop B', address='Address B', latitude=40.7473, longitude=-73.9860)
        Shop.objects.create(name='Shop C', address='Address C', latitude=40.7527, longitude=-73.9942)
        Shop.objects.create(name='Shop D', address='Address D', latitude=41.7589, longitude=-74.9851)

    def test_get_nearby_shops(self):
        url = reverse('get_nearby_shops')
        data = {'latitude': 40.7589, 'longitude': -73.9851, 'distance': 1}
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Shop A')
        self.assertEqual(response.data[1]['name'], 'Shop B')

