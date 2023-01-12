# Generated by Django 4.1 on 2023-01-07 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_mrmmodels'),
    ]

    operations = [
        migrations.CreateModel(
            name='AI_ML',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('language', models.EmailField(max_length=200, verbose_name='Language')),
                ('developer', models.CharField(max_length=25, verbose_name='Developer')),
            ],
        ),
    ]