# Generated by Django 5.1.6 on 2025-03-15 05:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('district', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taluka',
            fields=[
                ('taluka_id', models.AutoField(primary_key=True, serialize=False)),
                ('taluka_name', models.CharField(max_length=255)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='district.district')),
            ],
            options={
                'db_table': 'tbl_taluka',
            },
        ),
    ]
