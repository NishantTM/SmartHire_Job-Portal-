from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

<<<<<<< HEAD

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
=======
class User(AbstractUser):
    
        class Role(models.TextChoices):
        
            JOB_SEEKER = "JOB_SEEKER", "job_seeker",
            RECRUITER = "RECRUITER", "recruiter",
            ADMIN = "ADMIN", "admin"
        
        role = models.CharField(max_length=20, choices=Role.choices,default=Role.JOB_SEEKER)

        email = models.EmailField(unique=True)
        
        phone = models.CharField(max_length=15)
        
        profile_image = models.ImageField(upload_to="profile_images/", blank=True, null=True)
        
        created_at = models.DateField(auto_now_add=True)
        
        updated_at = models.DateField(auto_now=True)
        
        def __str__(self):
            return f"{self.username} - {self.get_role_display()}"
        
        
>>>>>>> 1bf5e7ac4d7554eaa72a7d6f65cb20b81b9d48b6
