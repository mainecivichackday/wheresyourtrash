import models

from rest_framework import serializers


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Provider
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'email_root', 
        )


