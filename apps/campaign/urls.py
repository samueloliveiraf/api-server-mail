from django.urls import path
from .views import (
    lists_campaign,
    send_emails_campaign,
    UpadateViewCampaign,
    CrieteViewCampaign,
    DeleteViewCampaign
)


urlpatterns = [
    path('lists-campaign/', lists_campaign, name='lists_campaigns'),
    path('send-emails-campaign/<int:id_campaign>/', send_emails_campaign, name='send_emails_campaign'),
    path('delete-campaign/<int:pk>/', DeleteViewCampaign.as_view(), name='delete_campaign'),
    path('update-campaign/<int:pk>/', UpadateViewCampaign.as_view(), name='update_campaign'),
    path('create-campaign/', CrieteViewCampaign.as_view(), name='create_campaign'),
]
