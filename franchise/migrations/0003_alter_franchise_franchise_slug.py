# Generated by Django 5.1.6 on 2025-03-26 04:42

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('franchise', '0002_alter_franchise_franchise_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='franchise',
            name='franchise_slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='franchise_name', unique=True),
        ),
    ]
