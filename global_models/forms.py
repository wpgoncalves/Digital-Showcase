from django import forms

from global_models.models import SocialNetworks


class SocialNetworksForm(forms.ModelForm):

    class Meta:
        model = SocialNetworks
        fields = '__all__'
