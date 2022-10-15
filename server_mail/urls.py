from django.urls import path, include
from django.contrib import admin

from apps.apis import urls as urls_api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls_api))
]
