from django.db import models
from django.contrib.auth import get_user_model
from .base import BaseModel


class Doctor(BaseModel):
    EDUCATION_TYPE = [
        ('general', 'General'),
        ('specialist', 'Specialist'),
        ('sub_specialist', 'Sub_Specialist'),
        ('fellowship', 'Fellowship')
    ]
    
    user = models.OneToOneField(get_user_model(),
                                on_delete=models.CASCADE,
                                related_name='doctors',
    )
    education = models.CharField(max_length=30,
                                 choices=EDUCATION_TYPE,
                                 default=EDUCATION_TYPE[0][0]
                                 )
    lisence = models.PositiveIntegerField()
    biography = models.TextField()
    category = models.ForeignKey('core.Category', on_delete=models.PROTECT, related_name='doctors') #Category.doctors.all()
    achive = models.CharField(max_length=128, null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True, blank=True)

    def __str__(self):
        return f'{self.user.phone_number}'