# Generated by Django 2.2 on 2019-06-02 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piusairline', '0006_auto_20190601_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='arrivalDate',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='departureDate',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='departureLocation',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='flightName',
        ),
        migrations.AddField(
            model_name='tickets',
            name='arrivalDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 2, 16, 26, 23, 724928)),
        ),
        migrations.AddField(
            model_name='tickets',
            name='departureAirport',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tickets',
            name='departureCountry',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tickets',
            name='departureDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='tickets',
            name='departureState',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tickets',
            name='destinationAirport',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tickets',
            name='destinationCountry',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tickets',
            name='destinationState',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tickets',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='ticketAuthor',
            field=models.IntegerField(null=True),
        ),
    ]
