# Generated by Django 4.1 on 2023-01-05 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_vendor_address_vendor_assets_vendor_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='address',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='assets',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='city',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='revenue',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='school',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='tenor',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='town',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='zipcode',
        ),
    ]
