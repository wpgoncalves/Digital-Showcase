from django import forms
from utils.tools import string_capitalize

from newsletter.models import Newsletter


class NewsletterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {
                'class': 'vTextField form-control text-capitalize',
                'placeholder': self.fields['name'].label,
                'required': True
            }
        )

        self.fields['email'].widget.attrs.update(
            {
                'class': 'vTextField form-control',
                'placeholder': 'name@example.com',
                'required': True
            }
        )

    def clean_name(self):
        return string_capitalize(self.cleaned_data['name'])

    class Meta:
        model = Newsletter
        fields = '__all__'
