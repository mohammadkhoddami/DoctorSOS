from django.urls import path, include



urlpatterns = [
    path('index/', include('api.endpoints.index', namespace='index'))
]

