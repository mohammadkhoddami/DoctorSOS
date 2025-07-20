from rest_framework import routers
from api.views import AppointmentViewSet


router =routers.DefaultRouter()

router.register('', AppointmentViewSet, basename='appointment')

urlpatterns = router.urls