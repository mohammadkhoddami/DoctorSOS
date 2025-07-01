from django.contrib import admin
from core.models import Category, Patient
from .models import User


admin.site.register(Category)
admin.site.register(User)
admin.site.register(Patient)