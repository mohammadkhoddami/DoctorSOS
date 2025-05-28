from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('category/', include('api.endpoints.category', namespace='category'))
]

