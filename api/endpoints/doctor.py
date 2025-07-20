from django.urls import path, include
from rest_framework_nested import routers
from api.views import DoctorViewSet, CommentViewSet

app_name = 'doctor'
 
router = routers.DefaultRouter() #type: ignore


router.register('', DoctorViewSet, basename='doctor')

doctor_router = routers.NestedDefaultRouter(router, '', lookup='doctor')
doctor_router.register(r'comments', CommentViewSet, basename='comment')

#127.0.0.1:8000/api/v1/doctors/{pk}/comments
#127.0.0.1:8000/api/v1/doctors/{pk}/comments/{pk}

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(doctor_router.urls))
]