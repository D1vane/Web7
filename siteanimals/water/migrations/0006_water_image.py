# Generated by Django 4.2.11 on 2024-04-29 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0005_alter_water_options_alter_water_facts_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='water',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/%Y/%m/%d/', verbose_name='Изображение'),
        ),
    ]
