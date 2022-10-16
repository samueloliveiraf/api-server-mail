from django.shortcuts import render
from .models import Campaign

import requests

from ..apis.views import send_email


def lists_campaign(request):
    campaigns = Campaign.objects.filter(
        user=request.user
    ).all()

    context = {'campaigns': campaigns}

    return render(request, 'campaign/list_campaigns.html', context)


def send_emails_campaign(request, id_campaign):
    campaigns = Campaign.objects.get(
        user=request.user,
        id=id_campaign
    )

    try:
        send_email(
            campaigns.subject,
            campaigns.image,
            campaigns.email_from,
            campaigns.emails_destiny,
            campaigns.color,
            campaigns.body
        )
        return render(request, 'campaign/list_campaigns.html')
    except Exception as e:
        print(f'Error ao enviar email {e}')

