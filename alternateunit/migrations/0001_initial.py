# Generated by Django 5.1.6 on 2025-03-21 05:01

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlternateUnit',
            fields=[
                ('alternateunit_id', models.AutoField(primary_key=True, serialize=False)),
                ('alternateunit_name', models.CharField(max_length=255, unique=True)),
                ('alternateunit_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='alternateunit_name', unique=True)),
            ],
            options={
                'db_table': 'tbl_alternateunit',
            },
        ),
    ]
