# Generated by Django 5.0.1 on 2024-01-24 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_videojuego_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Anime',
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='autor',
            field=models.CharField(default='Desconocido', max_length=30),
        ),
    ]
