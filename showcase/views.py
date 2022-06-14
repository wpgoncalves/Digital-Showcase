from django.contrib import messages
from django.views.generic import DetailView
from products.models import ProductImages, Products
from stores.models import Stores


class ShowcaseDetailView(DetailView):
    model = Stores
    context_object_name = 'store'
    template_name = 'showcase/showcase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        store_products = Products.objects.filter(
            owner_store__exact=context.get('store').cnpj).filter(
                discontinued__exact=False)

        context['store_products'] = store_products

        if not store_products:
            msg_empty_stores = 'Lamentamos mas ainda não há produtos \
                                cadastrados!'
            messages.add_message(self.request, messages.INFO, msg_empty_stores)
        else:
            store_products_img = ProductImages.objects.filter(
                product__in=store_products)

            context['store_products_img'] = store_products_img

        return context
