# Generated by Django 2.2 on 2019-06-01 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piusairline', '0004_auto_20190528_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='dateSold',
            field=models.DateTimeField(null=True),
        ),
    ]
