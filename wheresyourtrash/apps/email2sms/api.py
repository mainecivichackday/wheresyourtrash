from rest_framework import viewsets, permissions

from email2sms.models import Provider
from email2sms.serializers import ProviderSerializer

class ProviderViewSet(viewsets.ModelViewSet):
    """ViewSet for the Provider class"""

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [permissions.IsAuthenticated]


