from django.db import models
from .base import BaseModel


class DoctorProfile(BaseModel):
    EDUCATION_TYPE = [
        ('general', 'General'),
        ('specialist', 'Specialist'),
        ('sub_specialist', 'Sub_Specialist'),
        ('fellowship', 'Fellowship')
    ]
    
    
    education = models.CharField(max_length=30,
                                 choices=EDUCATION_TYPE,
                                 default=EDUCATION_TYPE[0][0]
                                 )
    lisence = models.PositiveIntegerField()
    #Likes Next Episode !
    biography = models.TextField()
    category = models.ForeignKey('core.Category', on_delete=models.PROTECT, related_name='doctors') #Category.doctors.all()
    achive = models.CharField(max_length=128, null=True, blank=True)
    schedule = models.DateTimeField() #since - till TODO: Change it To Model !  
    # picture = models.ImageField()
    vip = models.BooleanField(default=False)
    #need manager