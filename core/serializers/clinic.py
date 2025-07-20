from rest_framework import serializers
from core.models import ClinicInfo


class ClinicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicInfo
        fields = ('id', 'city', 'title', 'address', 'phone')