from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from django.views.generic import RedirectView


def main(request):
    return render(request, 'base/index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mall/', include('stores.urls')),
    path('', RedirectView.as_view(url='mall/')),
    path('main/', main, name='main')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
