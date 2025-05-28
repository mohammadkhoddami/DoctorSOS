from django.urls import path
from api.views import (CategoryListView,
                       CategoryDetailView
                       )

app_name = 'category'

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('<uuid:pk>/', CategoryDetailView.as_view(), name='category_detail')
]