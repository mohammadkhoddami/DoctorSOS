from django.db import models
from .base import BaseModel


class AppointMent(BaseModel):
    doctor = models.ForeignKey('core.Doctor', on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey('core.Patient', on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    doctor_note = models.TextField(null=True, blank=True)  #TODO CHANGE TO PATIENT NOTE
    
    #TODO Unique Together