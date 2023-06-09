# Generated by Django 4.2.1 on 2023-05-12 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_alter_tours_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tours',
            name='description',
            field=models.TextField(default='Тут должно быть описание тура', help_text='Описание тура', max_length=300),
        ),
        migrations.AlterField(
            model_name='tours',
            name='hotels_name',
            field=models.ForeignKey(help_text='Название отеля', max_length=60, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hotels_name', to='catalog.hotels'),
        ),
    ]
