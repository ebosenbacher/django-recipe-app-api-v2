"""
Django admin customisations
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']


# NOTE: second argument is to specify that we use the custom UserAdmin for managing the users
admin.site.register(models.user, UserAdmin)
