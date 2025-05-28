from django.db import models
from .base import BaseModel
from core.validators import validate_phone_number


class ClinicInfo(BaseModel):
    doctor = models.ForeignKey('core.Doctor', on_delete=models.CASCADE, related_name='clincs') #DoctorProfile.clincs.all()
    city = models.CharField(max_length=30)
    title = models.CharField(max_length=128)
    address = models.TextField()
    phone = models.CharField(max_length=11, validators=[validate_phone_number])
    