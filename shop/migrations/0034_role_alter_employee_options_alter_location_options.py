# Generated by Django 4.0.6 on 2022-11-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0033_alter_employee_employee_ref'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Undecided', max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['date_created']},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['date_created']},
        ),
    ]
