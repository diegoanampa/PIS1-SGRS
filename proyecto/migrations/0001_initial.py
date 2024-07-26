# Generated by Django 5.0.6 on 2024-07-18 04:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('ProCod', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('ProVer', models.CharField(max_length=50)),
                ('ProNom', models.CharField(max_length=255)),
                ('ProFecCre', models.DateField()),
                ('ProFecMod', models.DateField()),
                ('ProEst', models.CharField(max_length=50)),
                ('ProCom', models.TextField(blank=True)),
                ('ProCodModPlan', models.CharField(max_length=50)),
                ('ProOrgCod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
            ],
        ),
        migrations.CreateModel(
            name='ActaAcceptation',
            fields=[
                ('ActAceCod', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='proyecto.proyecto')),
                ('ActAceArc', models.FileField(upload_to='actas/')),
            ],
        ),
    ]
