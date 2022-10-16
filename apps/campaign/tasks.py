from celery.utils.log import get_task_logger
from django.core.mail import EmailMultiAlternatives

from server_mail.celery import app
from .models import Campaign
from ..apis.views import send_email

logger = get_task_logger(__name__)


@app.task(name='task_send_email', queue='queue_send_email')
def task_send_email(id_campaign):
    campaign = Campaign.objects.get(
        id=id_campaign
    )

    try:
        send_email(
            campaign.subject,
            campaign.image,
            campaign.email_from,
            campaign.emails_destiny,
            campaign.color,
            campaign.body
        )

        send_email(
            'Emais da Campanha enviado com sucesso!',
            campaign.image,
            campaign.email_from,
            campaign.email_from,
            campaign.color,
            'SUCESSO AO ENVIAR TODOS OS SEUS EMAILS!'
        )

    except Exception as e:
        print(f'Error ao enviar email {e}')
