# Generated by Django 4.0.6 on 2022-08-10 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_rename_customer_nu_customer_customer_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='date_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_ref',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
