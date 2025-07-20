from django.contrib import admin
from core.models import Category, Patient, Doctor, ClinicInfo
from .models import User


admin.site.register(Category)
admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(ClinicInfo)