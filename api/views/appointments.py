from rest_framework.viewsets import ModelViewSet
from core.serializers import AppointmentSerializer
from core.models import AppointMent


class AppointmentViewSet(ModelViewSet):
    queryset = AppointMent.objects.all().order_by('appointment_date', 'appointment_time')
    serializer_class = AppointmentSerializer
    # permission_classes = 
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return AppointMent.objects.all().order_by('appointment_date', 'appointment_time')
        return AppointMent.objects.filter(patient=self.request.user).order_by('appointment_date', 'appointment_time')
    
    def perform_create(self, serializer):
        user = self.request.user
        patient = user.patients
        if 'patient_id' in self.request.data:
            self.request.data.pop('patient_id')
        serializer.save(patient=patient)

#TODO
"""
1- Doctor --> pagination 1000 --> 10, 20 , 30
2- Filter --> psychology, general, heart, surgery
3- permission --> mr.x appointment dr.y --> Date, Time XXX 
TODO TASK{
    Appointment --> (action) <--
}
 




"""