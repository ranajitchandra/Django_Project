from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class custom_user(AbstractUser):
    user=[
        ('chef', 'Chrf'),('viewer', 'Viewer')
    ]
    display_name=models.CharField(max_length=100, null=True)
    age=models.CharField(max_length=10, null=True)
    city=models.CharField(max_length=100, null=True)
    country=models.CharField(max_length=100, null=True)
    user_type=models.CharField(choices=user, max_length=100, null=True)
    gender=models.CharField(max_length=100, null=True)
    user_image=models.ImageField(upload_to='static/user_img', null=True)
    
class add_recipe_model(models.Model):
    recipeTitle=models.CharField(max_length=100, null=True)
    ingredients=models.CharField(max_length=100, null=True)
    instructions=models.CharField(max_length=100, null=True)
    preparationTime=models.CharField(max_length=100, null=True)
    cookingTime=models.CharField(max_length=100, null=True)
    totalTime=models.CharField(max_length=100, null=True)
    nutritionalInfo=models.CharField(max_length=100, null=True)
    difficultyLevel=models.CharField(max_length=100, null=True)
    recipe_category=models.CharField(max_length=100, null=True)
    Tag_type=models.CharField(max_length=100, null=True)
    totalCalories=models.CharField(max_length=100, null=True)
    recipeImage=models.ImageField(upload_to='static/media', null=True)
    created_by=models.ForeignKey(custom_user, on_delete=models.CASCADE, null=True)
    
    
class chef_profile(models.Model):
    user_profile=models.OneToOneField(custom_user, on_delete=models.CASCADE)
    experience=models.CharField(max_length=100, null=True)
    skill=models.CharField(max_length=100, null=True)
    resume_latter=models.CharField(max_length=100, null=True)
    profile_img=models.ImageField(upload_to='static/profile_img', null=True)
    
    def __str__(self):
        return self.user_profile.display_name
    
class viewer_profile(models.Model):
    user_profile=models.OneToOneField(custom_user, on_delete=models.CASCADE)
    interest=models.CharField(max_length=100, null=True)
    profile_img=models.ImageField(upload_to='static/profile_img', null=True)
    
    def __str__(self):
        return self.user_profile.display_name
    
