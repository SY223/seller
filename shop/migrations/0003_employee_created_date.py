# Generated by Django 4.0.6 on 2022-07-24 20:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_items_product_item_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
