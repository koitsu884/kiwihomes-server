# Generated by Django 2.1.11 on 2019-08-28 22:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190819_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='uploads/property')),
                ('propertyType', models.CharField(max_length=50)),
                ('rooms', models.PositiveSmallIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.City')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Suburb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suburb', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.City')),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Region'),
        ),
        migrations.AddField(
            model_name='property',
            name='suburb',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Suburb'),
        ),
        migrations.AddField(
            model_name='property',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region'),
        ),
    ]