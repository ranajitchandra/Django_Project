# Generated by Django 5.0.4 on 2024-06-06 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobPortalApp', '0007_remove_jobapplymodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplymodel',
            name='status',
            field=models.CharField(default='Pending', max_length=100),
        ),
    ]
