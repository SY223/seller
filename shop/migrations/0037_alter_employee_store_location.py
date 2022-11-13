# Generated by Django 4.0.6 on 2022-11-12 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0036_alter_location_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='store_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='shop.location'),
        ),
    ]