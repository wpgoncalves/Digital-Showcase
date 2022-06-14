from django.urls import path

from stores import views

urlpatterns = [
    path('', views.StoresListView.as_view(), name='choose-store')
]
