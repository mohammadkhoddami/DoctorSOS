from django.db import transaction
from django.contrib.auth import get_user_model

from core.models import Doctor


@transaction.atomic
def create_doctor_and_user(validated_data):
    user_info = validated_data.pop('user')
    user = get_user_model().objects.create_user(**user_info)
    doctor = Doctor.objects.create(user=user,
                                   **validated_data)
    return doctor