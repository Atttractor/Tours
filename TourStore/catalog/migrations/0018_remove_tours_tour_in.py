# Generated by Django 4.2.1 on 2023-05-13 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_tours_tour_from_tours_tour_in'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tours',
            name='tour_in',
        ),
    ]
