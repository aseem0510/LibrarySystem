# Generated by Django 3.1.7 on 2021-04-16 08:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('need', '0004_auto_20210416_1355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookrecord',
            old_name='Id',
            new_name='key',
        ),
        migrations.AlterField(
            model_name='bookrecord',
            name='DueDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 1, 14, 2, 23, 96127)),
        ),
    ]