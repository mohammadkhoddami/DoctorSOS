from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models import Patient
from core.serializers import PatientSerializer


class PatientListView(ListCreateAPIView):
    queryset = Patient.objects.select_related('user').all()
    serializer_class = PatientSerializer



class PatientRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer