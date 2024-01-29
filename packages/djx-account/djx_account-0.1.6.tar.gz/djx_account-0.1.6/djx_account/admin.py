from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from djx_account.models import UserModel


class CustomAdmin(UserAdmin):
    list_display = ['username', 'email', 'email_confirmed']
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', {'fields': ('email_confirmed',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('email',),
        }),
    )


admin.site.register(UserModel, CustomAdmin)
