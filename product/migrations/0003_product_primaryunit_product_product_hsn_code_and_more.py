# Generated by Django 5.1.6 on 2025-03-21 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primaryunit', '0001_initial'),
        ('product', '0002_product_brands_product_category'),
        ('taxtype', '__first__'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='primaryunit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primaryunit.primaryunit'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_hsn_code',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='product_marathi_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='taxtype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taxtype.taxtype'),
        ),
    ]
