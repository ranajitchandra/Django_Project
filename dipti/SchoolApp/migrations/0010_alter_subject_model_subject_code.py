# Generated by Django 5.0.3 on 2024-05-30 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0009_subject_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject_model',
            name='subject_code',
            field=models.IntegerField(null=True),
        ),
    ]