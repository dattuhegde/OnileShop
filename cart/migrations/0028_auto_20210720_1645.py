# Generated by Django 2.2.12 on 2021-07-20 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0027_useraddress_cash_on_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='cash_on_delivery',
            field=models.CharField(default=True, max_length=10),
        ),
    ]
