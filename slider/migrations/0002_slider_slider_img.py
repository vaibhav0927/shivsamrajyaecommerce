# Generated by Django 5.1.6 on 2025-03-17 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='slider_img',
            field=models.ImageField(null=True, upload_to='slider/'),
        ),
    ]
