from .clinic import ClinicInfoSerializer
from .patient import UserInfo
from core.base import BaseDoctorSerializer
from core.services import create_doctor_and_user


class DoctorSerializer(BaseDoctorSerializer):
    pass


class CreateDoctorSerializer(BaseDoctorSerializer):
    user = UserInfo()
    clinics = ClinicInfoSerializer(read_only=True, many=True)
    
    class Meta(BaseDoctorSerializer.Meta):
        read_only_fields = [BaseDoctorSerializer.Meta.fields[8]]
        extra_kwargs = {
        'clinics': {'read_only': True}
    }
        
    def create(self, validated_data):
        return create_doctor_and_user(validated_data)