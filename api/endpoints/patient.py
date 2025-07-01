from django.urls import path
from api.views import PatientListView, PatientRetrieveUpdateDestroyView

app_name = 'patient'

urlpatterns = [
    path('', PatientListView.as_view(), name='patient'),
    path('<uuid:pk>/', PatientRetrieveUpdateDestroyView.as_view(), name='patient_detail')
]