# Generated by Django 4.0.6 on 2022-08-10 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_employee_store_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='store_location',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shop.location'),
        ),
    ]