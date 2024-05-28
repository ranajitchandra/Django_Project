from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=50, null=True)
    dep=models.CharField(max_length=50, null=True)
    email=models.EmailField(max_length=50, null=True)
    
    def __str__(self):
        return self.name + " " + self.dep


