# Generated by Django 5.1.6 on 2025-03-22 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_alternateunit'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='exp_date',
            field=models.DateField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='mfg_date',
            field=models.DateField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='mrp',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='op_qty',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='op_value',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='qrcode',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
