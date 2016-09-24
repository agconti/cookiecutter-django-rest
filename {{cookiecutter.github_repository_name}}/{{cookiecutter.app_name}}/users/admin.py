from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm

@admin.register(User)
class UserAdmin(AuthUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
