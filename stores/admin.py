from django.contrib import admin
from products.models import Products

from stores.forms import StoresForm
from stores.models import Stores


class ProductsInLine(admin.TabularInline):
    model = Products
    extra = 0
    fieldsets = (
        (None, {
            'fields': ('name', 'sale', 'discount', 'value', 'amount_stock',
                       'discontinued'),
        }),
    )


@admin.register(Stores)
class StoresAdmin(admin.ModelAdmin):
    form = StoresForm
    inlines = [ProductsInLine]
    list_display = ('business_name', 'cnpj', 'group',
                    'active', 'recorded', 'updated')
    search_fields = ('cnpj', 'business_name')
    list_filter = ('active', 'group')
    # list_editable = ('active',)
    prepopulated_fields = {'slug': ('title_establishment',)}
    fieldsets = (
        (None, {
            'fields':
            (
                'cnpj', 'business_name', 'title_establishment', 'group',
                ('address', 'address_number', 'address_complement'),
                ('phones', 'emails'), 'social_networks', 'slug', 'active'
            ),
            'description':
            '<h4><b>*Os campos em negrito são de preenchimento obrigatório.</b></h4>',  # noqa: E501
        }),
    )

    class Media:
        js = ('js/jquery.mask.min.js', 'stores/js/script.js')
