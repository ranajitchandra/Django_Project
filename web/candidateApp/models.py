from django.db import models

# Create your models here.

class candidate_model(models.Model):
    full_name=models.CharField(max_length=50, null=True)
    email=models.CharField(max_length=50, null=True)
    phone=models.CharField(max_length=50, null=True)
    address=models.CharField(max_length=50, null=True)
    img=models.ImageField(upload_to='media/candidate', null=True)
    
class student_model(models.Model):
    name=models.CharField(max_length=50, null=True)
    roll=models.CharField(max_length=10, null=True)
    lavel=models.CharField(max_length=50, null=True)
    std_img=models.ImageField(upload_to="media/student", null=True)