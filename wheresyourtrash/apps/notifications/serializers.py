from notifications import models

from rest_framework import serializers


class MunicipalitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Municipality
        fields = (
            'slug', 
            'id', 
            'name', 
            'created', 
            'updated', 
            'trashed', 
            'state', 
            'population', 
            'approved', 
        )


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.District
        fields = (
            'slug', 
            'id', 
            'name', 
            'created', 
            'updated', 
            'trashed', 
            'district_type', 
            'pickup_time', 
            'municipality',
        )


class DistrictExceptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DistrictExceptions
        fields = (
            'slug', 
            'id', 
            'name', 
            'created', 
            'updated', 
            'trashed', 
            'date', 
            'new_date', 
        )


class AddressBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AddressBlock
        fields = (
            'id', 
            'created', 
            'updated', 
            'address_range', 
            'district',
            'street', 
        )


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Subscription
        fields = (
            'id',
            'created',
            'updated',
            'trashed',
            'subscription_type',
            'phone_number',
            'service_provider',
        )


