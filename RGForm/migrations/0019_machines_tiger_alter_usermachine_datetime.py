# Generated by Django 4.1.5 on 2023-02-05 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RGForm', '0018_alter_usermachine_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='machines',
            name='Tiger',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='DateTime',
            field=models.CharField(default='05-02-2023 14:36:33', max_length=60, verbose_name='System ZeitstempelDerEingabe'),
        ),
    ]
