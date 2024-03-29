from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mall/', include('stores.urls')),
    path('about/', include('about.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('showcase/', include('showcase.urls')),
    path('customers/', include('customers.urls')),
    path('app/', include('app.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', RedirectView.as_view(url='mall/')),
    path('', include('pwa_fix.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
