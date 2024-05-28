from django.db import models

# Create your models here.

class personal_info(models.Model):
    name=models.CharField(max_length=30, null=True)
    address=models.CharField(max_length=50, null=True)
    occupation=models.CharField(max_length=50, null=True)
    phone=models.CharField(max_length=50, null=True)
    email=models.CharField(max_length=50, null=True)
    degree=models.CharField(max_length=50, null=True)
    summary=models.TextField(null=True)
    city=models.CharField(max_length=30, null=True)
    website=models.CharField(max_length=255, null=True)
    title=models.CharField(max_length=50, null=True)
    img=models.ImageField(upload_to="media/image", null=True)
    
class experience(models.Model):
    company_name=models.CharField(max_length=30, null=True)
    company_summary=models.TextField(null=True)
    company_address=models.CharField(max_length=50, null=True)
    company_role=models.CharField(max_length=20, null=True)
    company_joining=models.CharField(max_length=30)

class education(models.Model):
    s_name=models.CharField(max_length=50, null=True)
    s_lavel=models.CharField(max_length=50, null=True)
    s_point=models.CharField(max_length=50, null=True)
    s_year=models.CharField(max_length=50, null=True)
    s_address=models.CharField(max_length=50, null=True)


class skill(models.Model):
    s_html=models.CharField(max_length=30, null=True)
    s_css=models.CharField(max_length=30, null=True)
    s_js=models.CharField(max_length=30, null=True)
    s_python=models.CharField(max_length=30, null=True)
    s_php=models.CharField(max_length=30, null=True)
    s_sql=models.CharField(max_length=30, null=True)
