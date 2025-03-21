# Generated by Django 5.1.6 on 2025-03-18 07:22

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Primaryunit',
            fields=[
                ('primaryunit_id', models.AutoField(primary_key=True, serialize=False)),
                ('primaryunit_name', models.CharField(max_length=255, null=True)),
                ('primaryunit_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='primaryunit_name', unique=True)),
            ],
            options={
                'db_table': 'tbl_primaryunit',
            },
        ),
    ]
