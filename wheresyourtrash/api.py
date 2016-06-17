from rest_framework import routers

from notifications import api

router = routers.DefaultRouter()
router.register(r'municipalities', api.MunicipalityViewSet)
router.register(r'subscriptions', api.SubscriptionViewSet)
