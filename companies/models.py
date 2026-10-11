from django.db import models
from django.conf import settings

# from SmartHire.settings import AUTH_USER_MODEL

# Create your models here.

class Company(models.Model):
    
    recruiter = models.OneToOneField(settings.AUTH_USER_MODEL,
                                     on_delete=models.CASCADE, related_name='company')
    
    name = models.CharField(max_length=200)
    
    logo = models.ImageField(upload_to="company_logos/", blank=True, null=True)
    
    description = models.TextField()
    
    industry = models.CharField(max_length=200)
    
    website = models.URLField(blank=True)
    
    location = models.CharField(max_length=200)
    
    contact_email = models.EmailField(blank=True)
    
    contact_phone = models.CharField(max_length=15, blank=True)
    
    company_size = models.CharField(max_length=50, blank=True)
    
    founded_year = models.PositiveIntegerField(blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    
    updated_at = models.DateField(auto_now=True)
    
    
    def __str__(self):
        return self.name
