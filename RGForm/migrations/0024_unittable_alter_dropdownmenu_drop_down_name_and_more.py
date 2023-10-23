# Generated by Django 4.1.5 on 2023-02-10 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RGForm', '0023_alter_usermachine_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_for', models.CharField(max_length=40, null=True)),
                ('units', models.JSONField()),
            ],
        ),
        migrations.AlterField(
            model_name='dropdownmenu',
            name='drop_down_name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='Auftragsgeber',
            field=models.CharField(default='None', max_length=24),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='Betrieb',
            field=models.CharField(default='None', max_length=24),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='DateTime',
            field=models.CharField(default='11-02-2023 00:06:57', max_length=60, verbose_name='ZeitstempelDerEingabe'),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='Fahrer',
            field=models.CharField(default='None', max_length=24),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='Maschine',
            field=models.CharField(default='None', max_length=24),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='OrtDerTankung',
            field=models.CharField(default='None', max_length=24, verbose_name='Ort der Tankung'),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='Schlepper',
            field=models.CharField(default='None', max_length=24),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='Taetigkeit',
            field=models.CharField(default='None', max_length=24),
        ),
    ]
