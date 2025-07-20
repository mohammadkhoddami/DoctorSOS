from rest_framework.viewsets import ModelViewSet
from core.models import Doctor
from core.serializers import DoctorSerializer, CreateDoctorSerializer


class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateDoctorSerializer
        return DoctorSerializer