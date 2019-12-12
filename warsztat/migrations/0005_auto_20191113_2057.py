# Generated by Django 2.2.6 on 2019-11-13 19:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warsztat', '0004_auto_20191113_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.FloatField()),
                ('unit', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='cli_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 13, 20, 57, 37, 702624)),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partID', models.ManyToManyField(to='warsztat.Part')),
                ('repairID', models.ManyToManyField(to='warsztat.Repair')),
            ],
        ),
    ]