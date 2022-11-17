from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from products.models import Products
from products.serializers import ProductsSerializer


class ProductsList (ListAPIView):

    queryset = Products.objects.filter(discontinued__exact=False)
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductsDetail (RetrieveUpdateDestroyAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticated]
