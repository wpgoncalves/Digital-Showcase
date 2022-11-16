from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import api_root

urlpatterns = [
    path('', api_root, name='api-root')
]

urlpatterns = format_suffix_patterns(urlpatterns)
