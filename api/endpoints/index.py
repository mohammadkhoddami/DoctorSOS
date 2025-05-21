from django.urls import path
from api.views import IndexApiView

app_name = 'index'

urlpatterns = [
    path('home/', IndexApiView.as_view(), name='index_view')
]