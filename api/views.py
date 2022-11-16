from rest_framework.decorators import api_view
from rest_framework.response import Response

# from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 'customers': reverse('customers-list', request=request, format=format),
        # 'adresses': reverse('adresses-list', request=request, format=format)
    })
