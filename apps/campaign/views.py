from django.shortcuts import render
from .tasks import task_send_email
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
    campaign = Campaign.objects.get(
        user=request.user,
        id=id_campaign
    )

    task_send_email.delay(campaign.id)

    return render(request, 'campaign/list_campaigns.html')
