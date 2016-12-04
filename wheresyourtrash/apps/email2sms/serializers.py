from rest_framework import serializers

from email2sms.models import Provider

class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'email_root', 
        )


