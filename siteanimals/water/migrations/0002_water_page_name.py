# Generated by Django 4.2.10 on 2024-03-12 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='water',
            name='page_name',
            field=models.CharField(default='water', max_length=255),
        ),
    ]
