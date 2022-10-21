from django.urls import path

from app import views

app_name = 'app'

urlpatterns = [
    path('', views.app_install, name='app_install'),
]
