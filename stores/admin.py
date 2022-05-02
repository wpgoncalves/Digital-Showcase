from django.contrib import admin

from stores.forms import StoresForm
from stores.models import Stores


@admin.register(Stores)
class StoresAdmin(admin.ModelAdmin):
    form = StoresForm
    list_display = ('business_name', 'cnpj', 'active')
    search_fields = ('cnpj', 'business_name')
    list_filter = ('active',)
    list_editable = ('active',)
    prepopulated_fields = {'slug': ('title_establishment',)}
    fieldsets = (
        (None, {
            'fields':
            ('cnpj', 'business_name', 'title_establishment', 'slug', 'active'),
            'description':
            '<h4><b>*Os campos em negrito são de preenchimento obrigatório.</b></h4>',  # noqa: E501
        }),
    )

    class Media:
        js = ('js/jquery.mask.min.js', 'stores/js/script.js')
