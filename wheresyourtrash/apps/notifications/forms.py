from django import forms
from .models import Municipality, District, DistrictExceptions, AddressBlock, Subscription


class MunicipalityForm(forms.ModelForm):
    class Meta:
        model = Municipality
        fields = ['slug', 'name', 'updated', 'trashed', 'state', 'population', 'approved', 'contacts']


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ['slug', 'name', 'updated', 'trashed', 'district_type', 'pickup_time', 'municipality']


class DistrictExceptionsForm(forms.ModelForm):
    class Meta:
        model = DistrictExceptions
        fields = ['slug', 'name', 'updated', 'trashed', 'date', 'new_date', 'district']


class AddressBlockForm(forms.ModelForm):
    class Meta:
        model = AddressBlock
        fields = ['slug', 'name', 'updated', 'trashed', 'address_range', 'street', 'district']


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['slug', 'name', 'updated', 'trashed', 'subscription_type', 'user']


