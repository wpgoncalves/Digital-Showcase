from django.views.generic import DetailView, ListView

from stores.models import Stores


class StoresListView(ListView):
    # model = Stores
    template_name = 'stores/choose-store.html'
    queryset = Stores.objects.filter(active=True)


class StoresDetailView(DetailView):
    model = Stores
    template_name = 'stores/chosen-store.html'
