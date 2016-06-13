from django.contrib import admin
from django import forms
from .models import Municipality, District, DistrictExceptions, AddressBlock, Subscription

class MunicipalityAdminForm(forms.ModelForm):

    class Meta:
        model = Municipality
        fields = '__all__'


class MunicipalityAdmin(admin.ModelAdmin):
    form = MunicipalityAdminForm
    list_display = ['name', 'state', 'population', 'approved']
    readonly_fields = ['created', 'updated', 'trashed']

admin.site.register(Municipality, MunicipalityAdmin)


class DistrictAdminForm(forms.ModelForm):

    class Meta:
        model = District
        fields = '__all__'


class DistrictAdmin(admin.ModelAdmin):
    form = DistrictAdminForm
    list_display = ['name', 'created', 'updated', 'trashed', 'district_type', 'pickup_time']
    readonly_fields = ['created', 'updated', 'trashed']

admin.site.register(District, DistrictAdmin)


class DistrictExceptionsAdminForm(forms.ModelForm):

    class Meta:
        model = DistrictExceptions
        fields = '__all__'


class DistrictExceptionsAdmin(admin.ModelAdmin):
    form = DistrictExceptionsAdminForm
    list_display = ['id', 'slug', 'name', 'created', 'updated', 'trashed', 'date', 'new_date']
    readonly_fields = ['id', 'slug', 'name', 'created', 'updated', 'trashed', 'date', 'new_date']

admin.site.register(DistrictExceptions, DistrictExceptionsAdmin)


class AddressBlockAdminForm(forms.ModelForm):

    class Meta:
        model = AddressBlock
        fields = '__all__'


class AddressBlockAdmin(admin.ModelAdmin):
    form = AddressBlockAdminForm
    list_display = ['id', 'created', 'updated', 'address_range', 'street']
    readonly_fields = ['id', 'created', 'updated', 'address_range', 'street']

admin.site.register(AddressBlock, AddressBlockAdmin)


class SubscriptionAdminForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = '__all__'


class SubscriptionAdmin(admin.ModelAdmin):
    form = SubscriptionAdminForm
    list_display = ['id', 'created', 'updated', 'trashed', 'subscription_type', 'phone_number','service_provider']
    readonly_fields = ['id', 'created', 'updated', 'trashed', 'subscription_type', 'phone_number', 'service_provider']

admin.site.register(Subscription, SubscriptionAdmin)


