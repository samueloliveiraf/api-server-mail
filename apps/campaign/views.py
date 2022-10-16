from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView
)

from .tasks import task_send_email
from .models import Campaign


class UpadateViewCampaign(UpdateView):
    model = Campaign

    fields = [
        'subject',
        'image',
        'email_from',
        'emails_destiny',
        'color',
        'body'
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    template_name = 'campaign/update_campain.html'

    success_url = reverse_lazy('lists_campaigns')


class CrieteViewCampaign(CreateView):
    template_name = 'campaign/create_campaing.html'
    model = Campaign

    fields = [
        'subject',
        'image',
        'color',
        'email_from',
        'emails_destiny',
        'body'
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('lists_campaigns')


class DeleteViewCampaign(DeleteView):
    model = Campaign
    template_name = 'campaign/delete_campaing.html'

    success_url = reverse_lazy('lists_campaigns')


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

    return render(request, 'campaign/sucess_campaign.html')
