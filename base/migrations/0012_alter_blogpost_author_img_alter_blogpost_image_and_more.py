# Generated by Django 4.1.7 on 2023-11-10 15:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='author_img',
            field=models.ImageField(upload_to='Authors_images', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])]),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(upload_to='Blog-Images', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])]),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='gallery_image',
            field=models.ImageField(upload_to='Gallery_images', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])]),
        ),
    ]