# Generated by Django 3.1 on 2020-08-28 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200828_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qabul',
            name='photo',
            field=models.FileField(blank=True, upload_to='file/'),
        ),
    ]
