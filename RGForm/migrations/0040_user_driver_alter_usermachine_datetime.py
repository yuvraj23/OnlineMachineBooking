# Generated by Django 4.1.5 on 2023-02-26 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RGForm', '0039_user_alter_usermachine_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='driver',
            field=models.CharField(default='None', max_length=100, verbose_name='driver'),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='DateTime',
            field=models.CharField(default='26-02-2023 11:49:55', max_length=60, verbose_name='ZeitstempelDerEingabe'),
        ),
    ]
