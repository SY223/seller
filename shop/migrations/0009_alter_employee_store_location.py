# Generated by Django 4.0.6 on 2022-07-27 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_category_date_created_category_modified_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='store_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_store', to='shop.location'),
        ),
    ]
