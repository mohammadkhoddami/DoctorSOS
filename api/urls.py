from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('category/', include('api.endpoints.category', namespace='category')),
    path('auth/', include('api.endpoints.auth', namespace='auth')),
    path('patient/', include('api.endpoints.patient', namespace='patient')),
    path('doctor/', include('api.endpoints.doctor', namespace='doctor'))
]

