# Generated by Django 4.2.1 on 2023-05-12 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_hotels_hotel_pic_alter_tours_tour_pic_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travelcompanies',
            old_name='trave_company_pic',
            new_name='travel_company_pic',
        ),
    ]
