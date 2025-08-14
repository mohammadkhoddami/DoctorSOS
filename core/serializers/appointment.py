from rest_framework import serializers
from core.models import AppointMent


class AppointmentSerializer(serializers.ModelSerializer):
    patient = serializers.ReadOnlyField(source='appointment.patient.user.username')
    
    class Meta:
        model = AppointMent
        fields = ['patient', 'doctor', 'appointment_date', 'appointment_time', 'doctor_note']
        
    