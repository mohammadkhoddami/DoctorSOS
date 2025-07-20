from rest_framework import serializers
from core.models import Doctor
from core.serializers.clinic import ClinicInfoSerializer



class BaseDoctorSerializer(serializers.ModelSerializer):
    clinics = ClinicInfoSerializer(many=True)
    class Meta:
        model = Doctor
        fields = ['id' ,'user', 'clinics', 'education', 'lisence', 'biography', 'category', 'achive', 'rating']