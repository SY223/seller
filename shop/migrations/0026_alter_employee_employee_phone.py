# Generated by Django 4.0.6 on 2022-08-17 19:51

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_alter_employee_store_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=11, region=None),
        ),
    ]
