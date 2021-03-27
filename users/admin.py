from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from .models import User

class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(User, CustomUserAdmin)