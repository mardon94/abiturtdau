# Generated by Django 2.1.3 on 2020-08-31 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200831_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='title2',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='setting',
            name='address',
            field=models.TextField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='setting',
            name='company',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='setting',
            name='phone',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
