

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
