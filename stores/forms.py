from django import forms

from stores.models import Stores


class StoresForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StoresForm, self).__init__(*args, **kwargs)

        self.fields['cnpj'].widget.attrs['class'] += ' vMaskCnpjField'

    class Meta:
        model = Stores
        fields = '__all__'
