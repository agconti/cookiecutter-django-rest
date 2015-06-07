from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include('authentication.urls')),
    url(r'^api/v1/', include('users.urls')),
    url(r'^api/v1/notifications/', include('push_notifications.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
