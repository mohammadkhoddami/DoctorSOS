# Generated by Django 5.1.5 on 2025-07-13 16:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_doctor_comment_clinicinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinicinfo',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinics', to='core.doctor'),
        ),
    ]
