# Generated by Django 4.1.5 on 2023-03-05 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RGForm', '0044_alter_machines_cruiser_alter_machines_keine_maschine_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machines',
            name='Komoststreuer_1',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='machines',
            name='Komoststreuer_2',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='machines',
            name='Presse',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='DateTime',
            field=models.CharField(default='05-03-2023 09:28:36', max_length=60, verbose_name='ZeitstempelDerEingabe'),
        ),
    ]