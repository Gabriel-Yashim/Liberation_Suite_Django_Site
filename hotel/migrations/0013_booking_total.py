# Generated by Django 4.2.4 on 2023-09-06 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_remove_booking_guest_booking_booking_id_booking_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]
