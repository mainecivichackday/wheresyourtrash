import models
import serializers
from rest_framework import viewsets, permissions


class ProviderViewSet(viewsets.ModelViewSet):
    """ViewSet for the Provider class"""

    queryset = models.Provider.objects.all()
    serializer_class = serializers.ProviderSerializer
    permission_classes = [permissions.IsAuthenticated]


