# Generated by Django 4.2.11 on 2024-04-29 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0006_air_facts_air_kinds_airtags_air_class_of_animal_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='air',
            options={'verbose_name': 'Воздушные обитатели', 'verbose_name_plural': 'Воздушные обитатели'},
        ),
        migrations.AlterModelOptions(
            name='air_facts',
            options={'verbose_name': 'Интересный факт', 'verbose_name_plural': 'Интересный факт'},
        ),
        migrations.AlterField(
            model_name='air',
            name='animal',
            field=models.CharField(max_length=255, verbose_name='Имя животного'),
        ),
        migrations.AlterField(
            model_name='air',
            name='class_of_animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='air.air_kinds', verbose_name='Класс животного'),
        ),
        migrations.AlterField(
            model_name='air',
            name='content',
            field=models.TextField(blank=True, verbose_name='Текст о животном'),
        ),
        migrations.AlterField(
            model_name='air',
            name='is_red_book',
            field=models.BooleanField(choices=[(False, 'Распространенное'), (True, 'Редкое')], default=0, verbose_name='Красная книга'),
        ),
        migrations.AlterField(
            model_name='air',
            name='page_name',
            field=models.CharField(default='air', max_length=255, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='air',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='air.airtags', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='air',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='air',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Время изменения'),
        ),
        migrations.AlterField(
            model_name='air',
            name='unique_fact',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fact', to='air.air_facts', verbose_name='Факт о животном'),
        ),
        migrations.AlterField(
            model_name='air_kinds',
            name='name',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='airtags',
            name='tag',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Теги'),
        ),
    ]
