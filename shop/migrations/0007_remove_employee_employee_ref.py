# Generated by Django 4.0.6 on 2022-07-24 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_customer_store_customer_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee_ref',
        ),
    ]