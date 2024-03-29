# Generated by Django 4.2.2 on 2023-12-19 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0031_herosection'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image1',
            field=models.FileField(default='test', upload_to='hotel_gallery'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='image2',
            field=models.FileField(default='test', upload_to='hotel_gallery'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hotel',
            name='email',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='type',
            field=models.CharField(max_length=50),
        ),
    ]
