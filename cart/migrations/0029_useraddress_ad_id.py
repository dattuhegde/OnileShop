# Generated by Django 2.2.12 on 2021-07-29 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0028_auto_20210720_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='ad_id',
            field=models.CharField(default=True, max_length=100),
        ),
    ]