# Generated by Django 4.0.1 on 2022-03-28 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0006_alter_juego_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='imagen',
            field=models.ImageField(upload_to='juegos'),
        ),
    ]
