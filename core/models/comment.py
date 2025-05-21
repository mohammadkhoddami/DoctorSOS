from django.db import models
from .base import BaseModel


class Comment(BaseModel):
    COMMENT_STATUS = [
        ('waiting', 'Waiting'),
        ('approved', 'Approved'),
        ('notapproved', 'NotApproved'),
    ]
    
    doctor = models.ForeignKey('core.DoctorProfile', on_delete=models.CASCADE)
    author = models.ForeignKey('accounts.PaitentProfile', on_delete=models.CASCADE)
    body = models.TextField()
    status = models.CharField(max_length=15, choices=COMMENT_STATUS, default=COMMENT_STATUS[2][0])
    
    
    def __str__(self):
        return f'author : {self.author} , doctor: {self.doctor}'