from django.shortcuts import render


def app_install(request):
    return render(request, 'app/app_install.html')
