from django.test import TestCase
from django.urls import reverse

from stores.models import Stores


class ShowcaseURLsTest(TestCase):

    def test_showcase_url_is_correct(self):
        url = reverse('showcase:showcase', kwargs={'slug': 'tests-test'})
        self.assertEqual(url, '/showcase/tests-test/')


class ShowcaseViewsTest(TestCase):

    def create_fixture_store(
        self,
        cnpj='11111111111111',
        business_name='Test',
        title_establishment='Test',
        group='Test',
        slug='tests-test'
    ):
        return Stores.objects.create(
            cnpj=cnpj,
            business_name=business_name,
            title_establishment=title_establishment,
            group=group,
            slug=slug
        )

    # def test_stores_store_list_view_class_as_view_function_is_correct(self):
    #     request = RequestFactory().get(reverse('stores:choose-store'))
    #     view = views.StoresListView()
    #     view.setup(request)
    #     self.assertIs(view.as_view, views.StoresListView.as_view)

    def test_showcase_showcase_detail_view_return_status_code_200(self):
        store = self.create_fixture_store()  # fixture creation (store)
        url_store = reverse('showcase:showcase', kwargs={'slug': store.slug})
        response = self.client.get(url_store)
        self.assertEqual(response.status_code, 200)

    def test_showcase_showcase_detail_view_load_correct_template(self):
        store = self.create_fixture_store()  # fixture creation (store)
        url_store = reverse('showcase:showcase', kwargs={'slug': store.slug})
        response = self.client.get(url_store)
        self.assertTemplateUsed(response, 'showcase/showcase.html')

    def test_stores_choose_store_template_redirect_to_store_if_only_one_store_found(self):  # noqa: E501
        store = self.create_fixture_store()  # fixture creation (store)
        response = self.client.get(reverse('stores:choose-store'))
        url_store = reverse('showcase:showcase', kwargs={'slug': store.slug})
        self.assertIn(
            '<meta http-equiv="REFRESH" content="0;url=' + url_store + '"',
            response.content.decode('utf-8')
        )
        self.assertEqual(len(response.context['stores']), 1)
