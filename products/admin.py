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
            'fields': ('product', 'image', 'type'),
        }),
    )


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    form = ProductsForm
    inlines = [ProductImagesInLine]
    list_display = ('name', 'ean13code', 'sale', 'discount', 'value',
                    'amount_stock', 'discontinued')
    search_fields = ('name', 'ean13code')
    list_filter = ('sale', 'discontinued')
    fieldsets = (
        (None, {
            'fields': (('name', 'ean13code'), 'description', 'sale',
                       ('discount', 'value'), ('amount_stock',
                       'store_holder'), 'discontinued'),
            'description':
            '<h4><b>*Os campos em negrito são obrigatórios.</b></h4>',
        }),
    )
