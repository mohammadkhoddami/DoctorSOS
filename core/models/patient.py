from django.db import models
from .base import BaseModel
from django.contrib.auth import get_user_model

class Patient(BaseModel):
    user = models.OneToOneField(get_user_model(),
                                on_delete=models.CASCADE,
                                related_name='patients',
    )
    age = models.PositiveIntegerField()