from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
