from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=50, null=True)
    dep=models.CharField(max_length=50, null=True)
    email=models.EmailField(max_length=50, null=True)
    
    def __str__(self):
        return self.name + " " + self.dep



class teacher(models.Model):
    name= models.CharField(max_length=100, null=True)
    address= models.CharField(max_length=100, null=True)
    salary= models.CharField(max_length=100, null=True)
    
    
class employee(models.Model):
    name = models.CharField(max_length=100, null=True)
    emp_id = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.IntegerField( null=True)