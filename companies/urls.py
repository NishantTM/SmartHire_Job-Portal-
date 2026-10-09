from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.company_create, name="company_create"),
    
    path(
        "dashboard/",
        views.company_dashboard,
        name="company_dashboard",
    ),

    path(
        "profile/",
        views.company_detail,
        name="company_detail",
    ),

    path(
        "edit/",
        views.company_edit,
        name="company_edit",
    ),
]
