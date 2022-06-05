from django import forms
from utils.tools import string_capitalize

from customers.models import Customers


class CustomersForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CustomersForm, self).__init__(*args, **kwargs)

        self.fields['cpf_cnpj'].widget.attrs['class'] += ' vMaskCpfCnpjField'

        self.fields['passport'].widget.attrs['style'] = \
            'text-transform: uppercase;'

        fields_capitalize = [
            'name', 'responsible', 'country', 'address_complement'
        ]

        for i in fields_capitalize:
            self.fields[i].widget.attrs['style'] = \
                'text-transform: capitalize;'

    def clean_name(self):
        return string_capitalize(self.cleaned_data['name'])

    def clean_responsible(self):
        return string_capitalize(self.cleaned_data['responsible'])

    def clean_country(self):
        return string_capitalize(self.cleaned_data['country'])

    def clean_address_complement(self):
        return string_capitalize(self.cleaned_data['address_complement'])

    def clean_passport(self):
        return self.cleaned_data['passport'].upper()

    class Meta:
        model = Customers
        fields = '__all__'
