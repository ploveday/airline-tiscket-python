# Generated by Django 2.2 on 2019-06-01 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piusairline', '0005_auto_20190601_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='ticketAuthor',
            field=models.IntegerField(),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tickets',
            name='buyerID',
            field=models.IntegerField(null=True),
        ),
    ]