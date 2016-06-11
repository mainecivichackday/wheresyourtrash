from django.core.urlresolvers import reverse
from django.db.models import *
from django_extensions.db.fields import AutoSlugField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Provider(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    email_root = models.CharField(max_length=50)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('email2sms_provider_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('email2sms_provider_update', args=(self.slug,))


