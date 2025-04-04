# Generated by Django 5.1.6 on 2025-03-29 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0003_alter_customer_table'),
        ('order', '0002_delete_order'),
        ('product', '0005_product_barcode_product_exp_date_product_mfg_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('c_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'db_table': 'tbl_order',
            },
        ),
    ]
