from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class employee(models.Model):
    content = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE,)

class applyleave(models.Model):
    #==============================
    leavetype = [
        ('CL', 'CL'),
        ('EL', 'EL'),
        ('PL', 'PL'),
        ('TL', 'TL'),
    ]
    
    leave = models.CharField(
        max_length=10,
        choices=leavetype,
        default='CL',
    )

    holidayfrom = models.DateField(auto_now_add = False,auto_now=False,blank=False,default=datetime.date.today)
    holidayto = models.DateField(auto_now_add = False,auto_now=False,blank=False,default=datetime.date.today)
    detail = models.TextField()
    publish_date = models.DateField(auto_now_add=True)

    #====================================
    