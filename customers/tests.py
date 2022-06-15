from django.test import TestCase
from django.urls import reverse


class CustomersURLsTest(TestCase):

    def test_customers_register_url_is_correct(self):
        url = reverse('customers:register')
        self.assertEqual(url, '/customers/register/')

    def test_customers_validate_customer_register_url_is_correct(self):
        url = reverse('customers:validate_customer_register')
        self.assertEqual(url, '/customers/validate-customer-register/')
