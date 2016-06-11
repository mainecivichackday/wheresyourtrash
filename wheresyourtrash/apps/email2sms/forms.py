from django import forms
from .models import Provider


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['name', 'email_root']


