# Generated by Django 5.0.3 on 2024-05-29 03:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0007_rename_department_department_model_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_teacher_model',
            old_name='edu_qualofy',
            new_name='edu_qualify',
        ),
        migrations.RemoveField(
            model_name='add_teacher_model',
            name='password',
        ),
        migrations.RemoveField(
            model_name='add_teacher_model',
            name='t_email',
        ),
        migrations.RemoveField(
            model_name='add_teacher_model',
            name='t_username',
        ),
        migrations.RemoveField(
            model_name='add_teacher_model',
            name='teacher_id',
        ),
        migrations.AddField(
            model_name='add_teacher_model',
            name='dep_obj_add',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='SchoolApp.department_model'),
        ),
        migrations.AddField(
            model_name='add_teacher_model',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
