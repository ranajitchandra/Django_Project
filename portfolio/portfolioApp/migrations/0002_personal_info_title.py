# Generated by Django 5.0.4 on 2024-04-19 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_info',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]