# Generated by Django 3.2.3 on 2021-06-06 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='join_date',
            field=models.DateField(default=datetime.date(2021, 6, 6)),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(verbose_name=500)),
                ('order', models.ManyToManyField(to='main_app.Order')),
            ],
        ),
    ]
