# Generated by Django 5.0.4 on 2024-04-19 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0006_rename_skills_personal_info_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_html', models.CharField(max_length=30, null=True)),
                ('s_css', models.CharField(max_length=30, null=True)),
                ('s_js', models.CharField(max_length=50, null=True)),
                ('s_python', models.CharField(max_length=50, null=True)),
                ('s_php', models.CharField(max_length=50, null=True)),
                ('s_sql', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]