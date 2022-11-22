from django.contrib import admin

from stores.forms import StoresForm
from stores.models import Stores

# from products.models import Products


# class ProductsInLine(admin.TabularInline):
#     model = Products
#     extra = 0
#     fieldsets = (
#         (None, {
#             'fields': ('name', 'brand', 'sale', 'full_price', 'discount',
#                        'discount_price', 'discontinued'),
#         }),
#     )


@admin.register(Stores)
class StoresAdmin(admin.ModelAdmin):
    form = StoresForm
    # inlines = [ProductsInLine]
    list_display = ('business_name', 'cnpj', 'group', 'active')
    search_fields = ('cnpj', 'business_name')
    list_filter = ('active', 'group')
    # list_editable = ('active',)
    prepopulated_fields = {'slug': ('title_establishment',)}
    readonly_fields = ('recorded', 'updated')
    fieldsets = (
        (None, {
            'fields':
            ('cnpj', 'business_name', 'title_establishment', 'group', 'slug',
             'logo', 'active'),
            'description':
            '<h4><b>*Os campos em negrito são de preenchimento obrigatório.</b></h4>',  # noqa: E501
        }),
        ('Endereços', {
            'fields':
            (('address', 'address_number', 'address_complement')),
        }),
        ('Contatos e Mídias sociais', {
            'fields':
            (('phones', 'emails', 'social_networks')),
        }),
        ('Dados temporais', {
            'fields': ('recorded', 'updated')
        }),
    )

    class Media:
        js = ('js/jquery.mask.min.js', 'stores/js/script.js')
