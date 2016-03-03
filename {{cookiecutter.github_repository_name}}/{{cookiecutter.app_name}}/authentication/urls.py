from django.conf.urls import include, url
from rest_framework_jwt import views

urlpatterns = [
    url(r'^api-token-auth/', views.obtain_jwt_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
