from rest_framework import routers
from api.views import AppointmentViewSet

app_name = 'appointments'


router =routers.DefaultRouter()

router.register('', AppointmentViewSet, basename='appointment')

urlpatterns = router.urls