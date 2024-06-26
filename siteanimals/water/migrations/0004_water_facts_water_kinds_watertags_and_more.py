# Generated by Django 4.2.10 on 2024-04-05 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0003_alter_water_is_red_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Water_Facts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Water_Kinds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaterTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='water',
            name='class_of_animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='water.water_kinds'),
        ),
        migrations.AddField(
            model_name='water',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='water.watertags'),
        ),
        migrations.AddField(
            model_name='water',
            name='unique_fact',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fact', to='water.water_facts'),
        ),
    ]
