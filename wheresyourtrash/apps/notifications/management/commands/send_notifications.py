from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.mail import EmailMessage

import logging
logger = logging.getLogger(__name__)

from notifications.models import Subscription

FROM_EMAIL = getattr(settings, 'NOTIFICATION_FROM_EMAIL', 'notifications@wheresyourtrash.com')

class Command(BaseCommand):
    help = 'Run through subscriptions sending out notifications'

    def handle(self, *args, **options):
        # Gather all subscriptions that need to go out
        #subs = Subscription.objects.live()
        for sub in Subscription.objects.all():
            if sub.day_before_pickup:
                logger.info('Sending notification to {0}'.format(sub.user))
                template_name = sub.district.district_type.lower() + '_notification'
                if sub.subscription_type == 'SMS':
                    recipient = sub.clean_phone_number + '@' + sub.service_provider.email_root
                else:
                    recipient = sub.user.email
                txt_content = 'Is your trash outside and ready?'
                email = EmailMessage('Notification from WYT.com', txt_content, FROM_EMAIL, [recipient])
                email.send()

                '''
                send_templated_mail(template_name=template_name,
                                    from_email=FROM_EMAIL,
                                    recipient_list=[recipient],
                                    context={'subscription':sub})
                '''

