from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class custom_user(AbstractUser):
    USER=(
        ("1", "Admin"),
        ("2", "Teacher"),
        ("3", "Student"),
    )
    user_type=models.CharField(choices=USER, max_length=50, null=True)
    image=models.ImageField(upload_to="static/media/userIpic", null=True)
    
    def __str__(self):
        return self.username
class department(models.Model):
    department_name = models.CharField(max_length=100, null=True)
    department_head_name = models.CharField(max_length=100, null=True)
    create_date_at = models.DateField(auto_now=True, null=True)
    update_date_at = models.DateField(auto_now=True, null=True)


class add_student(models.Model):
    user=models.OneToOneField(custom_user,on_delete=models.CASCADE,null=True)
    f_name=models.CharField(max_length=100, null=True)
    l_name=models.CharField(max_length=100, null=True)
    std_id=models.CharField(max_length=100, null=True)
    gender=models.CharField(max_length=100, null=True)
    dob=models.CharField(max_length=100, null=True)
    religion=models.CharField(max_length=100, null=True)
    Joining_date=models.CharField(max_length=100, null=True)
    phone=models.CharField(max_length=100, null=True)
    section=models.CharField(max_length=100, null=True)
    img=models.ImageField(upload_to="static/media/student_pic", null=True)
    father_name=models.CharField(max_length=100, null=True)
    father_occu=models.CharField(max_length=100, null=True)
    father_phone=models.CharField(max_length=100, null=True)
    father_email=models.CharField(max_length=100, null=True)
    mother_name=models.CharField(max_length=100, null=True)
    mother_occu=models.CharField(max_length=100, null=True)
    mother_phone=models.CharField(max_length=100, null=True)
    mother_email=models.CharField(max_length=100, null=True)
    present_address=models.CharField(max_length=100, null=True)
    permanent_address=models.CharField(max_length=100, null=True)
    department_add=models.ForeignKey(department, on_delete=models.DO_NOTHING, null=True)
    
    
    

class add_teacher_model(models.Model):
    teacher_id = models.CharField(max_length=100, null=True)
    teacher_name = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=100, null=True)
    Joining_date = models.CharField(max_length=100, null=True)
    edu_qualofy = models.CharField(max_length=100, null=True)
    experience = models.PositiveIntegerField(max_length=100, null=True)
    t_username = models.CharField(max_length=100, null=True)
    t_email = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    present_address = models.CharField(max_length=100, null=True)
    permanent_address = models.CharField(max_length=100, null=True)
    t_img = models.ImageField(upload_to="static/media/teacher_pic", null=True)




    

    
class season(models.Model):
    start_season = models.CharField(max_length=50, null=True)
    end_season = models.CharField(max_length=50, null=True)