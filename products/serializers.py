# from rest_framework import serializers

# from products.models import Products


# class ProductsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Products

#         fields = [
#             'name',
#             'brand',
#             'description',
#             'discount_price',
#             'owner_store'
#         ]

from rest_framework import serializers

from products.models import Products


class ProductsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Products

        fields = [
            'name',
            'brand',
            'description',
            'discount_price',
            'owner_store'
        ]
