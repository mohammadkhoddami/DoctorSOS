from rest_framework import serializers
from core.models import AppointMent


class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.ReadOnlyField(source='appointment.doctor.user.username')
    patient = serializers.ReadOnlyField(source='appointment.patient.user.username')
    
    class Meta:
        model = AppointMent
        fields = ['appointment_date', 'appointment_time', 'doctor_note']
        
    