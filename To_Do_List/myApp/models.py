from django.db import models

from django.contrib.auth.models import AbstractUser


class customUser(AbstractUser):

    USER=[
        ("user","User"),
        ("admin","Admin"),
    ]

    city=models.CharField(max_length=100,null=True)
    profile_pic=models.ImageField(upload_to="media/Profile_Picture",null=True)
    user_type=models.CharField(choices=USER,max_length=100,null=True)

    class Meta:
        
        ordering=["last_name"]

        verbose_name="Custom User"

        db_table = "my_to_do_list_table"

        unique_together = ["username", "email"]

        verbose_name_plural = "Custom Users"


class CategoryModel(models.Model):

    user=models.ForeignKey(customUser,on_delete=models.CASCADE,null=True)
    CategoryName=models.CharField(max_length=100,null=True)
    create_at=models.DateField(auto_now_add=True,null=True)
    update_at=models.DateField(auto_now=True,null=True)

    def __str__(self) -> str:
        return self.CategoryName

class TaskModel(models.Model):

    PRIORITY=[
        ("high","High"),
        ("medium","Medium"),
        ("low","Low"),
    ]

    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    priority=models.CharField(choices=PRIORITY,max_length=100,null=True)
    TaskName=models.CharField(max_length=100,null=True)
    description=models.TextField(max_length=500,null=True)
    due_date=models.DateField(null=True)
    status=models.CharField(max_length=100,default="On_Going",null=True)
    completed_date=models.DateField(null=True)
    create_at=models.DateField(auto_now_add=True,null=True)
    update_at=models.DateField(auto_now=True,null=True)
    
    
    def __str__(self) -> str:
        return self.TaskName

    class Meta:

        unique_together = ["category", "TaskName"]



