
from django.urls import path

from customers import views

app_name = 'customers'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('validate-customer-register/', views.validate_customer_register,
         name='validate_customer_register')
]
