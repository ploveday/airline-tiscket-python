# Generated by Django 2.2 on 2019-05-24 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticketName', models.CharField(max_length=100)),
                ('ticketType', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateSold', models.DateTimeField()),
                ('buyerID', models.IntegerField()),
            ],
        ),
    ]
