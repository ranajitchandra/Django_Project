# Generated by Django 5.0.4 on 2024-04-19 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0009_alter_digree_dig_name_alter_hsc_h_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digree',
            name='dig_lavel',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hsc',
            name='h_lavel',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ssc',
            name='s_lavel',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
