from django.conf import settings
from django.contrib import messages
from django.views.generic import ListView
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from stores.models import Stores
from stores.serializers import StoreHyperlinkedSerializer, StoreSerializer


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


class StoreListCreateAPIView(ListCreateAPIView):

    queryset = Stores.objects.all()
    serializer_class = StoreHyperlinkedSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StoreRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Stores.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
