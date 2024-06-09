from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class Custom_user(AbstractUser):
    USER =  {
        ('user', 'USER'),
        ('admin', 'ADMIN')
    }
    city = models.CharField(max_length=100, null=True)
    profile_pic = models.ImageField(upload_to='static/media/profile_pic', null=True)
    user_type = models.CharField(choices=USER, max_length=100, null=True)
    
    class Meta:
        ordering = ['last_name']
        verbose_name = "Coustom User"
        db_table = "my_to_do_list_table"
        unique_together = ["username", "email"]
        verbose_name_plural = "Custom Users"
    
class categoryModel(models.Model):
    categoryName = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(Custom_user, on_delete=models.CASCADE, null=True)
    
class TaskModel(models.Model):
    
    PRIORITY = [
        ('high', 'HIGH'),
        ('medium', 'MEDIUM'),
        ('low', 'LOW'),
    ]
    category = models.ForeignKey(categoryModel, on_delete=models.CASCADE, null=True)
    priority = models.CharField(max_length=100, choices=PRIORITY, null=True)
    TaskName = models.CharField(max_length=100, null=True)
    status = models.CharField(default='On_Going', max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    due_Data = models.DateField(null=True)
    complite_Data = models.DateField(null=True)
    create_at = models.DateField(auto_now=True, null=True)
    update_at = models.DateField(auto_now=True, null=True)
    
    
    class Meta:
        unique_together = ["category", "TaskName"]
        ordering = ["category"]
        db_table = "My Task Model"