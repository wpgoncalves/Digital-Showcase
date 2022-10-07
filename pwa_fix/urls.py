from django.urls import path
from pwa.views import manifest, offline, service_worker

# Serve up serviceworker.js and manifest.json at the root
urlpatterns = [
    path('serviceworker.js', service_worker, name='serviceworker'),
    path('manifest.json', manifest, name='manifest'),
    path('offline/', offline, name='offline')
]
