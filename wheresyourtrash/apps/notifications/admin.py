from django.contrib import admin

from .models import Municipality, District, DistrictExceptions, AddressBlock, Subscription

admin.site.register(Municipality)
admin.site.register(District)
admin.site.register(DistrictExceptions)
admin.site.register(AddressBlock)
admin.site.register(Subscription)
