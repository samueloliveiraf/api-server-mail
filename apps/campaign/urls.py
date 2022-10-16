from django.urls import path
from .views import (
    lists_campaign,
    send_emails_campaign
)


urlpatterns = [
    path('lists-campaign/', lists_campaign, name='lists_campaigns'),
    path('send-emails-campaign/<int:id_campaign>/', send_emails_campaign, name='send_emails_campaign')
]
