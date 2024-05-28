from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class user_info_model(models.Model):
    name=models.CharField(max_length=50, null=True)
    email=models.CharField(max_length=50, null=True)
    user_pass=models.CharField(max_length=50, null=True)
    user_img=models.ImageField(upload_to='media/user_img', null=True)
    
    
class custom_user(AbstractUser):
    user_type=[
        ('admin', 'Admin'),
        ('viewer', 'viewer')
    ]
    display_name=models.CharField(max_length=100, null=True)
    user_type=models.CharField(choices=user_type, max_length=10, null=True)