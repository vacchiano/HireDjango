# Generated by Django 4.0.6 on 2022-08-13 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_level_role_business_job_title_business_website_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer',
            name='State',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='country',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='level',
            name='name',
            field=models.CharField(choices=[('Junior', 'Junior'), ('Mid-level', 'Mid'), ('Senior', 'Senior'), ('Principal', 'Principal'), ('C-level', 'CTO')], max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(choices=[('Part-time', 'Part-time'), ('Full-time', 'Full-time'), ('Contract', 'Contract')], max_length=50, unique=True),
        ),
    ]
