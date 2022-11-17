from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import api_root

urlpatterns = [
    path('', api_root, name='api-root'),
    path('products/', include('products.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
