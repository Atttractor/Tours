# Generated by Django 4.2.1 on 2023-05-12 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_tours_description_alter_travelcompanies_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='hotel_pic',
            field=models.ImageField(default='C:\\Users\\Dooplik\\Desktop\\Education\\Tours\\TourStore\\catalog\\static\\media\\cit.jpg', upload_to='img/companies_img/'),
        ),
        migrations.AddField(
            model_name='tours',
            name='tour_pic',
            field=models.ImageField(default='C:\\Users\\Dooplik\\Desktop\\Education\\Tours\\TourStore\\catalog\\static\\media\\cit.jpg', upload_to='img/tours_img/'),
        ),
    ]
