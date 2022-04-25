from django.urls import path

from stores import views

urlpatterns = [
    path('', views.choose_store, name='choose-store'),
    path('store-a/', views.store_a, name='store-a'),
    path('store-b/', views.store_b, name='store-b'),
    path('store-c/', views.store_c, name='store-c'),
]
