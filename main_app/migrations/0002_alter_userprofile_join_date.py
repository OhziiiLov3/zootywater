# Generated by Django 3.2.3 on 2021-05-15 00:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='join_date',
            field=models.DateField(default=datetime.date(2021, 5, 15)),
        ),
    ]
