from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
# Register your models here.



@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'username',
        'email',
        'role',
        'phone',
        'is_active',
        'date_joined',
    )

    list_filter = (
        'role',
        'is_active',
        'is_staff',
    )

    search_fields = (
        'username',
        'email',
        'phone',
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            'SmartHire Information',
            {
                'fields': (
                    'role',
                    'phone',
                    'profile_image',
                )
            }
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            'SmartHire Information',
            {
                'fields': (
                    'email',
                    'role',
                    'phone',
                    'profile_image',
                )
            }
        ),
    )