
# Generated by Django 5.1.6 on 2025-03-25 06:44

# Generated by Django 5.1.6 on 2025-03-25 05:37


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_img',
        ),
    ]
