from django.contrib import admin

from customers.forms import AdressesForm, CustomersForm, EmailsForm, PhonesForm
from customers.models import Adresses, Customers, Emails, Phones


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
        js = ('js/jquery.mask.min.js', 'customers/js/script.js')


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
        js = ('js/jquery.mask.min.js', 'customers/js/script.js')


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
