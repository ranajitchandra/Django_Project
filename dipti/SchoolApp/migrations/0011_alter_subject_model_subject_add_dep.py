# Generated by Django 5.0.3 on 2024-05-30 03:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0010_alter_subject_model_subject_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject_model',
            name='subject_add_dep',
            field=models.ForeignKey(max_length=20, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='SchoolApp.department_model'),
        ),
    ]
