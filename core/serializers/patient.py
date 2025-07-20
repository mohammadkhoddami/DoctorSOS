from rest_framework import serializers
from core.models import Patient
from django.contrib.auth import get_user_model
from core.services import create_user_and_patient


class UserInfo(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'phone_number', 'password']

    

class PatientSerializer(serializers.ModelSerializer):
    user = UserInfo()
    class Meta:
        model = Patient
        fields = ['id', 'user', 'age']
    
    def validate_age(self, data):
        if data > 110 or data < 1 :
            raise serializers.ValidationError("please put correct age")
        return data
    
    def create(self, validated_data):
        return create_user_and_patient(validated_data)