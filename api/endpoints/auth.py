from django.urls import path, re_path, include

app_name = 'auth'

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]