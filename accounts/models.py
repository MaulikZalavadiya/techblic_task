from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('solution_provider', 'Solution Provider'),
        ('solution_seeker', 'Solution Seeker'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)