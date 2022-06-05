from django.contrib import admin

from customers.forms import CustomersForm
from customers.models import Customers


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    form = CustomersForm
    raw_id_fields = ('address', 'phones', 'emails')
    radio_fields = {'kind': admin.HORIZONTAL}
    list_display = ('name', 'cpf_cnpj', 'kind')
    search_fields = ('cpf_cnpj', 'name')
    list_filter = ('kind',)
    fieldsets = (
        (None, {
            'fields': ('name', ('kind', 'cpf_cnpj'), ('ie_rg', 'responsible'),
                       ('passport', 'country'),
                       ('address', 'address_number', 'address_complement'),
                       ('phones', 'emails')),
            'description':
            '<h4><b>*Os campos em negrito são obrigatórios.</b></h4>',
        }),
    )

    class Media:
        js = ('js/jquery.mask.min.js', 'customers/js/script.js')
