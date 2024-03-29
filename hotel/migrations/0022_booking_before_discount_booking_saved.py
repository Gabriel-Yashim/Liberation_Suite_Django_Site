# Generated by Django 4.2.4 on 2023-09-07 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0021_remove_coupon_used_by_couponusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='before_discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AddField(
            model_name='booking',
            name='saved',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]
