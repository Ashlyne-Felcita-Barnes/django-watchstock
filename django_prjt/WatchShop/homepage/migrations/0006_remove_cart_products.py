# Generated by Django 4.2.14 on 2024-08-06 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_watchesuploads_count_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
    ]
