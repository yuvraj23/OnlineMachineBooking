# Generated by Django 4.1.5 on 2023-02-09 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RGForm', '0022_remove_dropdownmenu_dropdownname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermachine',
            name='DateTime',
            field=models.CharField(default='09-02-2023 21:15:41', max_length=60, verbose_name='ZeitstempelDerEingabe'),
        ),
    ]
