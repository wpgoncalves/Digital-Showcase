from django import forms
from utils.tools import string_capitalize

from global_models.models import Adresses, Emails, Phones, SocialNetworks


class AdressesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AdressesForm, self).__init__(*args, **kwargs)

        self.fields['cep'].widget.attrs['class'] += ' vMaskCepField'

        self.fields['address'].widget.attrs['style'] = \
            'text-transform: capitalize;'

        self.fields['district'].widget.attrs['style'] = \
            'text-transform: capitalize;'

        self.fields['city'].widget.attrs['style'] = \
            'text-transform: capitalize;'

    def clean_address(self):
        return string_capitalize(self.cleaned_data['address'])

    def clean_district(self):
        return string_capitalize(self.cleaned_data["district"])

    def clean_city(self):
        return string_capitalize(self.cleaned_data["city"])

    class Meta:
        model = Adresses
        fields = '__all__'


class PhonesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PhonesForm, self).__init__(*args, **kwargs)
        self.fields['number'].widget.attrs['class'] += ' vMaskPhoneField'

    class Meta:
        model = Phones
        fields = ('__all__')


class EmailsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmailsForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['style'] = \
            'text-transform: lowercase;'

    def clean_email(self):
        return self.cleaned_data['email'].lower()

    class Meta:
        model = Emails
        fields = '__all__'


class SocialNetworksForm(forms.ModelForm):

    class Meta:
        model = SocialNetworks
        fields = '__all__'
