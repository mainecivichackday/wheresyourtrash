from notifications import models
from notifications import serializers
from rest_framework import viewsets, permissions



class MunicipalityViewSet(viewsets.ModelViewSet):
    """ViewSet for the Municipality class"""

    queryset = models.Municipality.objects.all()
    serializer_class = serializers.MunicipalitySerializer
    permission_classes = [permissions.IsAuthenticated]


class DistrictViewSet(viewsets.ModelViewSet):
    """ViewSet for the District class"""

    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer
    permission_classes = [permissions.IsAuthenticated]


class DistrictExceptionsViewSet(viewsets.ModelViewSet):
    """ViewSet for the DistrictExceptions class"""

    queryset = models.DistrictExceptions.objects.all()
    serializer_class = serializers.DistrictExceptionsSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddressBlockViewSet(viewsets.ModelViewSet):
    """ViewSet for the AddressBlock class"""

    queryset = models.AddressBlock.objects.all()
    serializer_class = serializers.AddressBlockSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubscriptionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Subscription class"""

    queryset = models.Subscription.objects.all()
    serializer_class = serializers.SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]


