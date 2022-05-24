from django.urls import path

from newsletter import views

urlpatterns = [
    path('', views.subscribe, name='newsletter'),
    path('validate-subscribe/', views.validate_subscribe,
         name='validate_subscribe')
]
