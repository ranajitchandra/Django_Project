from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class customUserModel(AbstractUser):
    profile_picture = models.ImageField(upload_to='media/profilePic')
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(choices=GENDER, max_length=100)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now_add=True)
    USER_TYPE = [
        ('recruiter', 'Job_Recruiter'),
        ('seeker', 'Job_Seeker'),
    ]
    user_type = models.CharField(choices=USER_TYPE, max_length=100)

class job_model(models.Model):
    
    job_titel=models.CharField(max_length=40)
    company_name=models.CharField(max_length=40)
    address=models.CharField(max_length=40)
    job_desciption=models.CharField(max_length=40)
    company_desciption=models.CharField(max_length=40)
    qualification=models.CharField(max_length=40)
    salary=models.CharField(max_length=40)
    created_by = models.ForeignKey(customUserModel, on_delete=models.CASCADE,null=True)


    def __str__(self) -> str:
        return self.job_titel

class JobSeekerProfile(models.Model):
    user=models.OneToOneField(customUserModel,on_delete=models.CASCADE,related_name='jobseekerprofile')
    skils=models.CharField(max_length=40)
    work_experience=models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.user.first_name+ " " +self.user.last_name + " " + self.user.user_type


class JobRecruiterProfile(models.Model):
    user=models.OneToOneField(customUserModel,on_delete=models.CASCADE,related_name='jobrecruiterprofile')
    company_name=models.CharField(max_length=40)
    company_address=models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.user.first_name+ " " +self.user.last_name + " " + self.user.user_type

class BasicInformation(models.Model):
    user=models.OneToOneField(customUserModel,on_delete=models.CASCADE,related_name='basic_information')
    father_name=models.CharField(max_length=40)
    mother_name=models.CharField(max_length=40)

    
    def __str__(self) -> str:
        return self.user.first_name+ " " +self.user.father_name + " " + self.user.user_type


class jobApplyModel(models.Model):

    applicant=models.ForeignKey(customUserModel,on_delete=models.CASCADE,null=True)
    job=models.ForeignKey(job_model,on_delete=models.CASCADE,null=True)

    skills=models.CharField(max_length=40)
    profile_picture=models.ImageField(upload_to="media/seeker_image",null=True)
    resume=models.FileField(upload_to="media/seeker_resume",null=True)
    qualification=models.TextField(max_length=500,null=True)
    status=True