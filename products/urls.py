from django.urls import path

from products.views import ProductsDetail, ProductsList

urlpatterns = [
    path('', ProductsList().as_view(), name='products-list'),
    path('<int:pk>/', ProductsDetail().as_view(), name='products-detail')
]
