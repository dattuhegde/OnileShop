# Generated by Django 2.2.12 on 2021-07-20 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='add_description',
            field=models.TextField(blank=True),
        ),
    ]
