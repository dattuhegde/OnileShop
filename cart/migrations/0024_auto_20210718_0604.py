# Generated by Django 2.2.12 on 2021-07-18 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0023_auto_20210718_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='price',
            field=models.TextField(),
        ),
    ]
