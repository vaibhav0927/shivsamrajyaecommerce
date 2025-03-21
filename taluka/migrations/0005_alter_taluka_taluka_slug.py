# Generated by Django 5.1.6 on 2025-03-18 07:22

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taluka', '0004_taluka_taluka_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taluka',
            name='taluka_slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='taluka_name', unique=True),
        ),
    ]
