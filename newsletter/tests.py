from django.test import TestCase
from django.urls import resolve, reverse

from newsletter import views


class NewsletterURLsTest(TestCase):
    def test_newsletter_home_url_is_correct(self):
        url = reverse('newsletter:newsletter')
        self.assertEqual(url, '/newsletter/')

    def test_newsletter_validate_subscribe_url_is_correct(self):
        url = reverse('newsletter:validate_subscribe')
        self.assertEqual(url, '/newsletter/validate-subscribe/')


class StoresViewsTest(TestCase):

    def test_newsletter_home_views_function_is_correct(self):
        view = resolve(reverse('newsletter:newsletter'))
        self.assertIs(view.func, views.subscribe)

    def test_newsletter_validate_subscribe_views_function_is_correct(self):
        view = resolve(reverse('newsletter:validate_subscribe'))
        self.assertIs(view.func, views.validate_subscribe)

    def test_newsletter_subscribe_return_status_code_200(self):
        response = self.client.get(reverse('newsletter:newsletter'))
        self.assertEqual(response.status_code, 200)

    def test_newsletter_subscribe_load_correct_template(self):
        response = self.client.get(reverse('newsletter:newsletter'))
        self.assertTemplateUsed(response, 'newsletter/subscribe.html')
