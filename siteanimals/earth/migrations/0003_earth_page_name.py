# Generated by Django 4.2.10 on 2024-03-12 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earth', '0002_alter_uploadimage_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='earth',
            name='page_name',
            field=models.CharField(default='earth', max_length=255),
        ),
    ]
