# Generated by Django 5.0.3 on 2024-05-28 07:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0005_add_teacher_model_alter_add_student_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_student',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]