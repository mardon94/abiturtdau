# Generated by Django 2.1.3 on 2020-08-31 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20200831_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qabul',
            old_name='passport',
            new_name='pasport',
        ),
        migrations.RenameField(
            model_name='qabul',
            old_name='passport_photo',
            new_name='pasport_photo',
        ),
    ]
