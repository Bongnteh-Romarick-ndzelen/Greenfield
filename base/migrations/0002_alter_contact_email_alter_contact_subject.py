# Generated by Django 4.1.7 on 2023-11-06 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.TextField(blank=True),
        ),
    ]
