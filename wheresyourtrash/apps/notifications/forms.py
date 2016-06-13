from django import forms
from .models import Municipality, District, DistrictExceptions, AddressBlock, Subscription, SUB_TYPES
from email2sms.models import Provider
from custom_user.models import EmailUser as User


class MunicipalityForm(forms.ModelForm):
    class Meta:
        model = Municipality
        fields = ['name', 'trashed', 'state', 'population', 'approved', 'contacts']


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ['name', 'trashed', 'district_type', 'pickup_time', 'municipality']


class DistrictExceptionsForm(forms.ModelForm):
    class Meta:
        model = DistrictExceptions
        fields = ['name', 'trashed', 'date', 'new_date', 'district']


class AddressBlockForm(forms.ModelForm):
    class Meta:
        model = AddressBlock
        fields = ['address_range', 'street', 'district']


class SubscriptionForm(forms.ModelForm):
    service_provider = forms.ModelChoiceField(queryset=Provider.objects.all(), label="Mobile phone service provider", required=False)
    subscription_type = forms.ChoiceField(choices=SUB_TYPES, widget=forms.RadioSelect())
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Subscription
        fields = ['subscription_type', 'phone_number', 'service_provider', 'user', 'district']


