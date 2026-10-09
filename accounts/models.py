from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    class Role(models.TextChoices):
        JOB_SEEKER = 'JOB_SEEKER', 'Job Seeker'
        RECRUITER = 'RECRUITER', 'Recruiter'
        ADMIN = 'ADMIN', 'Admin'

    email = models.EmailField(unique=True)

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.JOB_SEEKER
    )

    profile_image = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )   

    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username