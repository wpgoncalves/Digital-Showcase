from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from products.models import Products
from products.serializers import ProductHyperlinkedSerializer


class ProductListCreateAPIView(ListCreateAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductHyperlinkedSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductHyperlinkedSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
