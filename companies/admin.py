from django.contrib import admin

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