from django.contrib import admin
<<<<<<< HEAD
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
=======

# Register your models here.
>>>>>>> 1bf5e7ac4d7554eaa72a7d6f65cb20b81b9d48b6
