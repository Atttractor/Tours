import datetime
import uuid
from django.db import models
from django.urls import reverse


class Countries(models.Model):
    name = models.CharField(primary_key=True, max_length=60,
                            help_text="Название страны")

    def __str__(self):
        return self.name


class Airlines(models.Model):
    name = models.CharField(primary_key=True, max_length=45,
                            help_text='Название авиакомпании')
    country_name = models.ForeignKey(Countries, max_length=60,
                                     help_text='Страна базирования',
                                     on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TravelCompanies(models.Model):
    name = models.CharField(primary_key=True, max_length=30, help_text="Название туристической компании")
    travel_company_pic = models.ImageField(upload_to='img/companies_img',
                                           default=r'C:\Users\Dooplik\Desktop\Education\Tours\TourStore\catalog\static'
                                                   r'\media\cit.jpg')
    city = models.CharField(max_length=60, help_text='Город базирования')
    addres = models.CharField(max_length=100, help_text='Адрес')
    phone_number = models.CharField(max_length=11, help_text='Номер телефона')
    mail = models.EmailField(help_text='Электронная почта')
    country_name = models.ForeignKey(Countries, max_length=60,
                                     help_text='Страна базирования',
                                     on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('travelcompanies-detail', args=[str(self.pk)])


class Hotels(models.Model):
    name = models.CharField(primary_key=True, max_length=30, help_text='Название отеля')
    hotel_pic = models.ImageField(upload_to='img/hotels_img',
                                  default=r'C:\Users\Dooplik\Desktop\Education\Tours\TourStore\catalog\static\media'
                                          r'\cit.jpg')
    all_rooms = models.IntegerField(help_text='Всего номеров')
    available_rooms = models.IntegerField(help_text='Свободных номеров')
    pool = models.BooleanField(null=True, help_text='Есть ли бассеин?')
    buffet = models.BooleanField(null=True, help_text='Есть ли шведский стол?')
    bar = models.BooleanField(null=True, help_text='Есть ли бар?')
    country_name = models.ForeignKey(Countries, max_length=60,
                                     help_text='Страна базирования',
                                     on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tours(models.Model):
    name = models.CharField(primary_key=True, max_length=45, help_text='Название тура')
    tour_pic = models.ImageField(upload_to='img/tours_img', default=r'C:\Users\Dooplik\Desktop\Education\Tours'
                                                                    r'\TourStore\catalog\static\media\cit.jpg')
    description = models.TextField(max_length=300, help_text='Описание тура', default='Тут должно быть описание тура')
    id = models.UUIDField(default=uuid.uuid4, help_text="Уникальный идентификатор")
    start_date = models.DateField(help_text='Дата начала тура', default=datetime.datetime.now)
    end_date = models.DateField(help_text='Дата окончания тура', default=datetime.datetime.now)
    city = models.CharField(max_length=30, help_text='Город')
    price = models.FloatField(help_text='Цена тура')
    travel_complany_name = models.ForeignKey(TravelCompanies, max_length=60,
                                             help_text='Туристическая компания',
                                             on_delete=models.CASCADE,
                                             to_field='name',
                                             related_name='travel_complany_name')
    hotels_name = models.ForeignKey(Hotels, max_length=60,
                                    help_text='Название отеля',
                                    on_delete=models.SET_NULL,
                                    to_field='name',
                                    null=True,
                                    related_name='hotels_name')
    flights_name = models.ManyToManyField(Airlines, through='Flights')
    tour_from = models.ForeignKey(Countries, max_length=60,
                                  help_text='Откуда летим',
                                  on_delete=models.CASCADE,
                                  related_name='tour_from',
                                  default='Россия')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tours-detail', args=[str(self.pk)])


class Flights(models.Model):
    tour_name = models.ForeignKey(Tours, on_delete=models.CASCADE,
                                  help_text='Название тура', to_field='name',
                                  related_name='tour_name')
    airline_name = models.ForeignKey(Airlines, on_delete=models.CASCADE,
                                     help_text='Название авиакомпании',
                                     to_field='name',
                                     related_name='airlines_name')


class Buyers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Уникальный идентификатор")
    first_name = models.CharField(max_length=20, help_text='Имя')
    last_name = models.CharField(max_length=20, help_text='Фамилия')
    phone_number = models.CharField(max_length=11, help_text='Номер телефона')
    mail = models.EmailField(help_text='Электронная почта', null=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Basket(models.Model):
    buyers_id = models.ForeignKey(Buyers, on_delete=models.CASCADE,
                                  help_text='id покупателя')
    tours_name = models.ForeignKey(Tours, on_delete=models.CASCADE,
                                   help_text='название тура')

    def __str__(self):
        return f'{self.buyers_id}, {self.tours_name}'
