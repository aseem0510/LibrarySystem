# Generated by Django 3.1.7 on 2021-04-21 10:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('need', '0006_auto_20210421_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrecord',
            name='DueDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 15, 41, 26, 76871)),
        ),
    ]