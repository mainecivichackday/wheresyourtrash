from django.contrib import admin
from django import forms
from .models import Provider

class ProviderAdminForm(forms.ModelForm):

    class Meta:
        model = Provider
        fields = '__all__'


class ProviderAdmin(admin.ModelAdmin):
    form = ProviderAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'email_root']
    readonly_fields = ['slug', 'created', 'last_updated']

admin.site.register(Provider, ProviderAdmin)


