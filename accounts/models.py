from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICE = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    ]
    
    
    phone_number = models.CharField(max_length=11, unique=True)
    role = models.CharField(max_length=8, choices=ROLE_CHOICE, default=ROLE_CHOICE[1][0])
