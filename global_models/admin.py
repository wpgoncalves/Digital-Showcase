from django.contrib import admin

from global_models.forms import SocialNetworksForm
from global_models.models import SocialNetworks


@admin.register(SocialNetworks)
class SocialNetworksAdmin(admin.ModelAdmin):
    form = SocialNetworksForm
    list_display = ('url', 'media')
    search_fields = ('url',)
    list_filter = ('media',)
    fieldsets = (
        (None, {
            'fields':
            ('url', 'media'),
            'description':
            '<h4><b>*Os campos em negrito são de preenchimento obrigatório.</b></h4>',  # noqa: E501
        }),
    )
