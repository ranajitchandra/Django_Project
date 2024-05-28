# Generated by Django 5.0.3 on 2024-05-27 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100, null=True)),
                ('department_head_name', models.CharField(max_length=100, null=True)),
                ('create_date_at', models.DateField(auto_now=True, null=True)),
                ('update_date_at', models.DateField(auto_now=True, null=True)),
            ],
        ),
    ]