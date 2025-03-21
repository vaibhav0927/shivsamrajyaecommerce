
# Generated by Django 5.1.6 on 2025-03-21 04:33

# Generated by Django 5.1.6 on 2025-03-18 07:22


import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('village', '0002_village_village_slug_alter_village_taluka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='village',
            name='village_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='village',
            name='village_slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='village_name', unique=True),
        ),
    ]
