# Generated by Django 4.2.4 on 2023-09-06 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0013_booking_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total_days',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
