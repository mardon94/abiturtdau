# Generated by Django 3.0.8 on 2020-08-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200826_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qabul',
            name='d_photo',
            field=models.ImageField(blank=True, upload_to='file/'),
        ),
        migrations.AlterField(
            model_name='qabul',
            name='p_photo',
            field=models.ImageField(blank=True, upload_to='file/'),
        ),
        migrations.AlterField(
            model_name='qabul',
            name='photo',
            field=models.ImageField(blank=True, upload_to='file/'),
        ),
    ]