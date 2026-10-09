from django.contrib import admin

<<<<<<< HEAD
from .models import Company

# Register your models here.

@admin.register(Company)

class CompanyAdmin(admin.ModelAdmin):
    
    list_display = (
           "name",
        "recruiter",
        "industry",
        "location",
        "created_at",
    )

    search_fields = (
        "name",
        "industry",
        "location",
        "recruiter__username",
    )

    list_filter = (
        "industry",
        "location",
    )
=======
# Register your models here.
>>>>>>> 1bf5e7ac4d7554eaa72a7d6f65cb20b81b9d48b6
