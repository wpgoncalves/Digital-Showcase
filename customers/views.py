from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render


def register(request):
    msg_empty_stores = 'Teste TESTE teste!'
    messages.add_message(request, messages.ERROR, msg_empty_stores)

    return render(request, 'customers/customer-registration-form.html')


def validate_customer_register(request):
    return HttpResponse('<h1>!!! REGISTRED (Test) !!!</h1>')
