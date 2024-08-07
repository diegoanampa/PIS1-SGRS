# Generated by Django 5.0.6 on 2024-07-18 04:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('ArtCod', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('AtNom', models.CharField(max_length=255)),
                ('ArtNem', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationType',
            fields=[
                ('TipOrgCod', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('TipOrgNom', models.CharField(max_length=255)),
                ('TipOrgDes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('OrgCod', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('OrgVer', models.CharField(max_length=50)),
                ('OrgNom', models.CharField(max_length=255)),
                ('OrgFecCre', models.DateField()),
                ('OrgFecMod', models.DateField()),
                ('OrgCodModPlan', models.CharField(max_length=50)),
                ('OrgAutCod', models.CharField(max_length=50)),
                ('OrgDir', models.CharField(max_length=255)),
                ('OrgTel', models.IntegerField()),
                ('OrgRepLeg', models.CharField(max_length=255)),
                ('OrgTelRepLeg', models.IntegerField()),
                ('OrgRuc', models.IntegerField()),
                ('OrgContact', models.CharField(max_length=255)),
                ('OrgTelCon', models.CharField(max_length=50)),
                ('OrgCom', models.CharField(max_length=255)),
                ('OrgArtCod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.artifact')),
                ('OrgTipOrgCod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organizationtype')),
            ],
        ),
    ]
