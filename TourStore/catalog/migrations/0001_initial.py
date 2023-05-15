# Generated by Django 4.2.1 on 2023-05-08 13:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airlines',
            fields=[
                ('name', models.CharField(help_text='Название авиакомпании', max_length=45, primary_key=True, serialize=False)),
                ('country_name', models.CharField(help_text='Страна базирования', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Buyers',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Уникальный идентификатор', primary_key=True, serialize=False)),
                ('first_name', models.CharField(help_text='Имя', max_length=20)),
                ('last_name', models.CharField(help_text='Фамилия', max_length=20)),
                ('phone_number', models.CharField(help_text='Номер телефона', max_length=11)),
                ('mail', models.EmailField(help_text='Электронная почта', max_length=254, null=True)),
                ('tour_name', models.CharField(help_text='Название тура', max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('name', models.CharField(help_text='Название страны', max_length=60, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('name', models.CharField(help_text='Название отеля', max_length=30, primary_key=True, serialize=False)),
                ('all_rooms', models.IntegerField(help_text='Всего номеров')),
                ('available_rooms', models.IntegerField(help_text='Свободных номеров')),
                ('pool', models.BooleanField(help_text='Есть ли бассеин?', null=True)),
                ('buffet', models.BooleanField(help_text='Есть ли шведский стол?', null=True)),
                ('bar', models.BooleanField(help_text='Есть ли бар?', null=True)),
                ('country_name', models.CharField(help_text='Страна базирования', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('name', models.CharField(help_text='Нзвание тура', max_length=45, primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField(help_text='Дата начала тура')),
                ('end_date', models.DateTimeField(help_text='Дата окончания тура')),
                ('city', models.CharField(help_text='Город', max_length=30)),
                ('price', models.FloatField(help_text='Цена тура')),
                ('travel_complany_name', models.CharField(help_text='Туристическая компания', max_length=60)),
                ('hotels_name', models.CharField(help_text='Названеи отеля', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TravelCompanies',
            fields=[
                ('name', models.CharField(default=uuid.uuid4, help_text='Название туристической компании', max_length=30, primary_key=True, serialize=False)),
                ('city', models.CharField(help_text='Город базирования', max_length=60)),
                ('addres', models.CharField(help_text='Адрес', max_length=100)),
                ('phone_number', models.CharField(help_text='Номер телефона', max_length=11)),
                ('mail', models.EmailField(help_text='Электронная почта', max_length=254)),
                ('country_name', models.CharField(help_text='Страна базирования', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline_name', models.ForeignKey(help_text='Название авиакомпании', on_delete=django.db.models.deletion.CASCADE, related_name='airlines_name', to='catalog.airlines')),
                ('tour_name', models.ForeignKey(help_text='Название тура', on_delete=django.db.models.deletion.CASCADE, related_name='tour_name', to='catalog.tours')),
            ],
        ),
    ]