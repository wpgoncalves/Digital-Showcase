from django.test import TestCase
from django.urls import reverse


class StoresURLsTest(TestCase):
    def test_stores_url_is_correct(self):
        url = reverse('stores:choose-store')
        self.assertEqual(url, '/mall/')
