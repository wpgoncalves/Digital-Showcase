from django.urls import path

from stores import views

urlpatterns = [
    path('', views.StoresListView.as_view(), name='choose-store'),
    path('<slug:slug>/', views.StoresDetailView.as_view(), name='chosen-store'),  # noqa:E501
]
