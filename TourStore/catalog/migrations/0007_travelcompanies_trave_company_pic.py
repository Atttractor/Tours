# Generated by Django 4.2.1 on 2023-05-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_hotels_hotel_pic_tours_tour_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelcompanies',
            name='trave_company_pic',
            field=models.ImageField(default='C:\\Users\\Dooplik\\Desktop\\Education\\Tours\\TourStore\\catalog\\static\\media\\cit.jpg', upload_to='img/companies_img/'),
        ),
    ]
