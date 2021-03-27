from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from django.views.decorators.csrf import csrf_exempt

from .views import SignupView

urlpatterns = [
    path("login/", obtain_auth_token, name="login"),
    path("signup/", SignupView.as_view(), name="signup")
]