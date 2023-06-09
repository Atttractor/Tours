# Generated by Django 4.2.1 on 2023-05-11 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_tours_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tours',
            name='description',
            field=models.TextField(default='Тут должно быть описание тура', help_text='Описание тура', max_length=300),
        ),
        migrations.AlterField(
            model_name='travelcompanies',
            name='name',
            field=models.CharField(help_text='Название туристической компании', max_length=30, primary_key=True, serialize=False),
        ),
    ]
