# Generated by Django 2.2.6 on 2019-11-16 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warsztat', '0006_auto_20191113_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='clientID',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='service',
            name='cli_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 16, 20, 20, 22, 727307)),
        ),
    ]
