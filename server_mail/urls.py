from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib import admin

from apps.apis import urls as urls_api
from apps.campaign import urls as urls_campaigns
from apps.core.views import home, index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls_api)),
    path('campaigns/', include(urls_campaigns)),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),


    path('home/', home, name='home'),
    path('', index, name='index')
]
