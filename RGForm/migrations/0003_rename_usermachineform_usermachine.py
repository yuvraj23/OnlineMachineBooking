# Generated by Django 4.1.5 on 2023-01-21 22:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RGForm', '0002_rename_user_usermachineform_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserMachineForm',
            new_name='UserMachine',
        ),
    ]