# Generated by Django 5.0.6 on 2024-07-24 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_especificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilacion',
            name='IlaVer',
            field=models.FloatField(),
        ),
    ]
