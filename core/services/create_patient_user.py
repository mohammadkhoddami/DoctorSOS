from django.db import transaction
from django.contrib.auth import get_user_model
from core.models import Patient


@transaction.atomic
def create_user_and_patient(validated_data):
        user_data = validated_data.pop('user')
        user = get_user_model().objects.create_user(**user_data)
        patient = Patient.objects.create(user=user, **validated_data)
        return patient