# Generated by Django 5.0.6 on 2024-07-18 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artifact',
            old_name='AtNom',
            new_name='ArtNom',
        ),
    ]
