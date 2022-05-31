from django.conf import settings
from django.contrib import messages
from django.views.generic import DetailView, ListView
from products.models import ProductImages, Products

from stores.models import Stores


class StoresListView(ListView):
    context_object_name = 'stores'
    template_name = 'stores/choose-store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group_stores_images'] = settings.GROUP_STORES_IMAGES
        return context

    def get_queryset(self):
        queryset = Stores.objects.filter(active=True)

        if not queryset:
            msg_empty_stores = 'Lamentamos mas ainda não há lojas cadastradas!'
            messages.add_message(self.request, messages.INFO, msg_empty_stores)

        return queryset


class StoresDetailView(DetailView):
    model = Stores
    context_object_name = 'store'
    template_name = 'stores/chosen-store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        store_products = Products.objects.filter(
            store_holder=context.get('store').cnpj).filter(discontinued=False)

        store_products_img = ProductImages.objects.filter(
            product__in=store_products)

        context['store_products'] = store_products
        context['store_products_img'] = store_products_img
        return context
