from django.shortcuts import render


def choose_store(request):
    return render(request, 'stores/main/home.html')


def store_a(request):
    return render(request, 'stores/store_a/home.html')


def store_b(request):
    return render(request, 'stores/store_b/home.html')


def store_c(request):
    return render(request, 'stores/store_c/home.html')
