from django import forms
from django.utils.text import slugify

from stores.models import Stores


class StoresForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StoresForm, self).__init__(*args, **kwargs)

        self.fields['cnpj'].widget.attrs['class'] += ' vMaskCnpjField'
        self.fields['slug'].widget.attrs['readonly'] = True

    def clean_slug(self):
        data = self.cleaned_data['slug']

        if 'title_establishment' in self.cleaned_data:
            data = slugify(self.cleaned_data['title_establishment'])

        return data

    class Meta:
        model = Stores
        fields = '__all__'
