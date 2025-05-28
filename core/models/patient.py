from django.db import models
from .base import BaseModel


class Patient(BaseModel):
    age = models.PositiveIntegerField()