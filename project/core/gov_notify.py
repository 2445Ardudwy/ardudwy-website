import os

from django.conf import settings

from notifications_python_client.notifications import NotificationsAPIClient

GOV_NOTIFY_API_KEY=settings.GOV_NOTIFY_APIS['DEV_KEY'] if settings.DEBUG else settings.GOV_NOTIFY_APIS['LIVE_KEY']

notifications_client = NotificationsAPIClient(GOV_NOTIFY_API_KEY)

class SendEmail():
    def send_email_notification_staff(email_to, full_name, subject, email, tel_num, message, sent_to_list):
        notifications_client.send_email_notification(
            email_address=email_to,
            template_id="8f532910-8fd1-4520-ae18-a480be8e23dd",
            personalisation={
                'full_name': full_name,
                'subject': subject,
                'email': email,
                'tel_num': tel_num,
                'message': message,
                'email_to': ', '.join(sent_to_list)
            },
        )

    def send_email_notification_user(email_to, full_name, subject, first_name):
        notifications_client.send_email_notification(
            email_address=email_to,
            template_id="27254b07-470d-4224-902c-e8ed7f42a015",
            personalisation={
                'full_name': full_name,
                'subject': subject,
                'first_name': first_name,
            },
        )