# Generated by Django 2.2 on 2019-05-26 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piusairline', '0002_sales'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airlineusers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('userid', models.CharField(max_length=100)),
                ('country', models.TextField()),
                ('state', models.TextField()),
                ('regdate', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField()),
                ('description', models.TextField()),
                ('special', models.TextField()),
            ],
        ),
    ]
