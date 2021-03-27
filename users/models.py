from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class User(AbstractUser):

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
