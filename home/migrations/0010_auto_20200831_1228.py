# Generated by Django 2.1.3 on 2020-08-31 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200828_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qabul',
            name='photo',
            field=models.FileField(blank=True, upload_to='file/'),
        ),
    ]
