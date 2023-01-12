# Generated by Django 4.1 on 2023-01-01 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_employee_created_at_employee_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('industry', models.CharField(max_length=25, verbose_name='Industry')),
            ],
        ),
    ]