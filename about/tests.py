from django.test import TestCase
from django.urls import reverse


class AboutURLsTest(TestCase):

    def test_about_home_url_is_correct(self):
        url = reverse('about:about')
        self.assertEqual(url, '/about/')
