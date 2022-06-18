from django.test import TestCase
from django.urls import resolve, reverse

from about import views


class AboutURLsTest(TestCase):

    def test_about_home_url_is_correct(self):
        url = reverse('about:about')
        self.assertEqual(url, '/about/')


class StoresViewsTest(TestCase):

    def test_about_home_views_function_is_correct(self):
        view = resolve(reverse('about:about'))
        self.assertIs(view.func, views.about)

    def test_about_home_return_status_code_200(self):
        response = self.client.get(reverse('about:about'))
        self.assertEqual(response.status_code, 200)

    def test_about_home_load_correct_template(self):
        response = self.client.get(reverse('about:about'))
        self.assertTemplateUsed(response, 'about/about.html')
