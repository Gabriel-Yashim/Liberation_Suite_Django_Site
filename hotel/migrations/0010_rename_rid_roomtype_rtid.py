# Generated by Django 3.2.18 on 2023-07-31 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_auto_20230731_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomtype',
            old_name='rid',
            new_name='rtid',
        ),
    ]
