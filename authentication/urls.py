from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from authentication.api import LoginView

urlpatterns=[
    url(r'v1/auth/login/$', csrf_exempt(LoginView.as_view()), name='login'),
]