# Generated by Django 4.2.2 on 2024-01-24 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0040_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
