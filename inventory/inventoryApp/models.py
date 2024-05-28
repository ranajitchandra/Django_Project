from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class custom_user(AbstractUser):
    user=[
        ('admin', 'Admin'),
        ('viewer', 'Viewer')
    ]
    display_name=models.CharField(max_length=100, null= True)
    user_type=models.CharField(choices=user, max_length=100, null= True)
    image=models.ImageField(upload_to='static/media', null= True)
    
class add_data(models.Model):
    title=models.CharField(max_length=100, null=True)
    c_name=models.CharField(max_length=100, null=True)
    c_des=models.CharField(max_length=100, null=True)
    which_user=models.ForeignKey(custom_user, on_delete=models.CASCADE, null=True)