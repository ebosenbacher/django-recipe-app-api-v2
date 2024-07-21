"""
Django admin customisations
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_("Additional information"), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']


# NOTE: second argument is to specify that we use t
# he custom UserAdmin for managing the users
admin.site.register(models.user, UserAdmin)
