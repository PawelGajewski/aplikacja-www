# Generated by Django 2.2.6 on 2019-11-24 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warsztat', '0013_auto_20191120_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='cli_date',
            field=models.DateField(default='1970-01-01'),
        ),
    ]