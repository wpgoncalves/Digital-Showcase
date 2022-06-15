from django.test import TestCase
from django.urls import reverse


class NewsletterURLsTest(TestCase):
    def test_newsletter_home_url_is_correct(self):
        url = reverse('newsletter:newsletter')
        self.assertEqual(url, '/newsletter/')

    def test_newsletter_validate_subscribe_url_is_correct(self):
        url = reverse('newsletter:validate_subscribe')
        self.assertEqual(url, '/newsletter/validate-subscribe/')
