
# Generated by Django 5.1.6 on 2025-03-17 05:29

from django.db import migrations
<<<<<<< HEAD

# Generated by Django 5.1.6 on 2025-03-16 08:02

from django.db import migrations # type: ignore

=======
# Generated by Django 5.1.6 on 2025-03-16 08:02

from django.db import migrations # type: ignore
>>>>>>> 3a5d205939989e96a82c8d642034e2c794a24292


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_district_customer_franchise_customer_state_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='tbl_customer',
        ),
    ]
