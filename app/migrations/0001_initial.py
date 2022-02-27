# Generated by Django 4.0 on 2022-02-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField(max_length=15, verbose_name='Температура')),
                ('humidity', models.IntegerField(max_length=15, verbose_name='Влажность')),
                ('pressure', models.IntegerField(max_length=15, verbose_name='Давление')),
                ('rain_chance', models.IntegerField(max_length=15, verbose_name='Вероятность дождя')),
                ('part_of_the_day', models.CharField(max_length=35, verbose_name='Часть дня')),
            ],
        ),
    ]