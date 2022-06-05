from django.contrib import admin

from global_models.forms import (AdressesForm, EmailsForm, PhonesForm,
                                 SocialNetworksForm)
from global_models.models import Adresses, Emails, Phones, SocialNetworks


@admin.register(Adresses)
class AdressesAdmin(admin.ModelAdmin):
    form = AdressesForm
    list_display = ('__str__', 'district', 'cep', 'city', 'state')
    search_fields = ('cep', 'address')
    list_filter = ('type', 'city', 'district', 'state')
    fieldsets = (
        (None, {
            'fields': ('cep', ('type', 'address'),
                       ('district', 'city', 'state')),
            'description':
            '<h4><b>*Os campos em negrito são obrigatórios.</b></h4>',
        }),
    )

    class Media:
        js = ('js/jquery.mask.min.js', 'global_models/js/script.js')


@admin.register(Phones)
class PhonesAdmin(admin.ModelAdmin):
    form = PhonesForm
    list_display = ('type', 'number')
    search_fields = ('number',)
    list_filter = ('type',)
    fieldsets = (
        (None, {
            'fields': ('number', 'type', 'comments'),
            'description':
            '<h4><b>*Os campos em negrito são obrigatórios.</b></h4>',
        }),
    )

    class Media:
        js = ('js/jquery.mask.min.js', 'global_models/js/script.js')


@admin.register(Emails)
class EmailsAdmin(admin.ModelAdmin):
    form = EmailsForm
    list_display = ('email',)
    search_fields = ('email',)
    fieldsets = (
        (None, {
            'fields': ('email', ),
            'description':
            '<h4><b>*Os campos em negrito são obrigatórios.</b></h4>',
        }),
    )


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
