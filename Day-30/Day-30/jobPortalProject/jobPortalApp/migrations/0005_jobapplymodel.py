# Generated by Django 5.0.4 on 2024-06-05 04:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobPortalApp', '0004_basicinformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='jobApplyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=40)),
                ('profile_picture', models.ImageField(null=True, upload_to='media/seeker_image')),
                ('resume', models.FileField(null=True, upload_to='media/seeker_resume')),
                ('qualification', models.TextField(max_length=500, null=True)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobPortalApp.job_model')),
            ],
        ),
    ]