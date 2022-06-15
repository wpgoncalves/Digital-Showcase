from django.test import TestCase
from django.urls import reverse


class ShowcaseURLsTest(TestCase):
    def test_showcase_url_is_correct(self):
        url = reverse('showcase:showcase', kwargs={'slug': 'tests-test'})
        self.assertEqual(url, '/showcase/tests-test/')
