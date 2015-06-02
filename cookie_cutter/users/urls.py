from __future__ import unicode_literals

from django.conf.urls import url

import views

urlpatterns = [
    url(r'^users/', views.UserView.as_view(), name='users-list'),
]
