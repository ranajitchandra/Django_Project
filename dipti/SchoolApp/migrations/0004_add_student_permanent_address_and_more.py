# Generated by Django 5.0.3 on 2024-05-28 05:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0003_add_student_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_student',
            name='permanent_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='add_student',
            name='present_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='add_student',
            name='department_add',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='SchoolApp.department'),
        ),
        migrations.AlterField(
            model_name='add_student',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
