# Generated by Django 2.2.12 on 2021-07-18 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0024_auto_20210718_0604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddress',
            name='payment',
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='price',
            field=models.IntegerField(),
        ),
    ]
