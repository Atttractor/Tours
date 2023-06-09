# Generated by Django 4.2.1 on 2023-05-14 13:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_alter_tours_end_date_alter_tours_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tours',
            name='end_date',
            field=models.DateField(default=datetime.datetime.now, help_text='Дата окончания тура'),
        ),
        migrations.AlterField(
            model_name='tours',
            name='start_date',
            field=models.DateField(default=datetime.datetime.now, help_text='Дата начала тура'),
        ),
    ]
