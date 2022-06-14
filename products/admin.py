from django.contrib import admin

from products.forms import ProductsForm
from products.models import ProductImages, Products


class ProductImagesInLine(admin.TabularInline):
    model = ProductImages
    extra = 0
    min_num = 1
    max_num = 3
    fieldsets = (
        (None, {
            'fields': ('image', 'type'),
        }),
    )


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    form = ProductsForm
    inlines = [ProductImagesInLine]
    list_display = ('name', 'brand', 'ean13code', 'sale', 'full_price',
                    'discount', 'discount_price', 'discontinued')
    search_fields = ('name', 'ean13code')
    list_filter = ('sale', 'discontinued', 'brand')
    readonly_fields = ('recorded', 'updated')
    fieldsets = (
        (None, {
            'fields': (('name', 'brand', 'ean13code'), 'description'),
            'description':
            '<h4><b>*Os campos em negrito são obrigatórios.</b></h4>',
        }),
        ('Dados de comercialização', {
            'fields': ('sale', ('full_price', 'discount', 'discount_price'),
                       'discontinued')
        }),
        ('Loja detentora', {
            'fields': ('owner_store',)
        }),
        ('Dados temporais', {
            'fields': ('recorded', 'updated')
        }),
    )
