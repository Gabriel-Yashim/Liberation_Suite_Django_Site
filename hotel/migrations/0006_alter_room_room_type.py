# Generated by Django 3.2.18 on 2023-07-31 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_auto_20230731_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('King', 'King'), ('Luxury', 'Luxury'), ('Normal', 'Normal'), ('Economic', 'Economic')], max_length=10),
        ),
    ]
