<<<<<<< HEAD
# Generated by Django 5.1.6 on 2025-03-15 05:32
=======
<<<<<<< HEAD
# Generated by Django 5.1.6 on 2025-03-15 05:35
=======
# Generated by Django 5.1.6 on 2025-03-15 05:31
>>>>>>> 1d8badf4145db30e2dee1b49669009ab38678376
>>>>>>> 897d0039814bfa032952a565bc85b2ca3b115a68

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taluka', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Village',
            fields=[
                ('village_id', models.AutoField(primary_key=True, serialize=False)),
                ('village_name', models.CharField(max_length=255)),
                ('taluka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taluka.taluka')),
            ],
            options={
                'db_table': 'tbl_village',
            },
        ),
    ]
