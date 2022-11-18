from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import api_root
from products.views import (ProductListCreateAPIView,
                            ProductRetrieveUpdateDestroyAPIView)
from stores.views import (StoreListCreateAPIView,
                          StoreRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('', api_root, name='api-root'),
    path('products/', include([
        path('', ProductListCreateAPIView().as_view(), name='products-list'),
        path('<int:pk>/', ProductRetrieveUpdateDestroyAPIView().as_view(),
             name='products-detail')
    ])),
    path('stores/', include([
        path('', StoreListCreateAPIView().as_view(), name='stores-list'),
        path('<int:pk>', StoreRetrieveUpdateDestroyAPIView().as_view(),
             name='stores-detail')
    ]))
]

urlpatterns = format_suffix_patterns(urlpatterns)
