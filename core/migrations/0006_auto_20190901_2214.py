# Generated by Django 2.1.11 on 2019-09-01 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190901_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(upload_to='uploads/property'),
        ),
    ]
