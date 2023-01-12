# Generated by Django 4.1 on 2022-12-31 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 12, 31, 5, 15, 53, 556246, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='notes',
            field=models.TextField(default=datetime.datetime(2022, 12, 31, 5, 16, 4, 746372, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]