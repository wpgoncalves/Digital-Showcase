from rest_framework import serializers

from stores.models import Stores


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stores

        fields = [
            'cnpj',
            'business_name',
            'title_establishment',
            'slug',
            'group',
            'active'
        ]


class StoreHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):

    cnpj = serializers.HyperlinkedIdentityField(
        view_name='stores-detail'
    )

    class Meta:
        model = Stores

        fields = [
            'cnpj',
            'business_name',
            'title_establishment',
            'slug',
            'group',
            'active'
        ]
