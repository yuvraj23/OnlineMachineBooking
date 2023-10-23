# Generated by Django 4.1.5 on 2023-02-07 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RGForm', '0020_alter_usermachine_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='DropDownMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dropDownName', models.CharField(default='None', max_length=40)),
                ('list_of_choice', models.JSONField()),
            ],
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='DateTime',
            field=models.CharField(default='07-02-2023 21:55:53', max_length=60, verbose_name='ZeitstempelDerEingabe'),
        ),
    ]