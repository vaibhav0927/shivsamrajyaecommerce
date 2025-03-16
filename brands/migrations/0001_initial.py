# Generated by Django 5.1.6 on 2025-03-15 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('brands_id', models.AutoField(primary_key=True, serialize=False)),
                ('brands_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tbl_brands',
            },
        ),
    ]
