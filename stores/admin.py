from django.contrib import admin
from products.models import Products

from stores.forms import SocialNetworksForm, StoresForm
from stores.models import SocialNetworks, Stores


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
    list_display = ('business_name', 'cnpj', 'group', 'active')
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
                ('phones', 'emails'), 'slug', 'active'
            ),
            'description':
            '<h4><b>*Os campos em negrito são de preenchimento obrigatório.</b></h4>',  # noqa: E501
        }),
    )

    class Media:
        js = ('js/jquery.mask.min.js', 'stores/js/script.js')


@admin.register(SocialNetworks)
class SocialNetworksAdmin(admin.ModelAdmin):
    form = SocialNetworksForm
    list_display = ('store_holder', 'media', 'url')
    search_fields = ('store_holder', 'url')
    list_filter = ('media',)
    fieldsets = (
        (None, {
            'fields':
            ('store_holder', ('media', 'url')),
            'description':
            '<h4><b>*Os campos em negrito são de preenchimento obrigatório.</b></h4>',  # noqa: E501
        }),
    )
