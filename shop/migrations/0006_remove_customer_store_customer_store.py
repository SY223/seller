# Generated by Django 4.0.6 on 2022-07-24 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_employee_store_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='store',
        ),
        migrations.AddField(
            model_name='customer',
            name='store',
            field=models.ManyToManyField(related_name='store_location', to='shop.location'),
        ),
    ]
