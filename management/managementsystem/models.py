from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class extendemp(models.Model):
    catagory_type = [
        ('ADID', 'ADID'),
        ('UNADID', 'UNADID'),
        ('STUFF', 'STUFF'),
    ]

    department_type = [
        ('ARTS', 'ARTS'),
        ('SCIENCE', 'SCIENCE'),
        ('COMMERCE', 'COMMERCE'),
    ]
    catagory = models.CharField(max_length=15,choices=catagory_type,default='ADID',)
    department = models.CharField(max_length=15,choices=department_type,default='ARTS',)
    phone = models.CharField(max_length=10)

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    
