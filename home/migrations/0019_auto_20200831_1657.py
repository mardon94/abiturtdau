# Generated by Django 2.1.3 on 2020-08-31 11:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20200831_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='company',
            field=ckeditor.fields.RichTextField(),
        ),
    ]