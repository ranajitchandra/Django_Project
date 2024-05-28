from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Custom_User_Model(AbstractUser):
    USEER_TYPE=[
        ('admin', 'Admin'), ('genaral', 'Genaral')
    ]
    User_name= models.CharField(max_length=100)
    User_password=models.CharField(max_length=20)
    User_type=models.CharField(choices=USEER_TYPE, max_length=100)
