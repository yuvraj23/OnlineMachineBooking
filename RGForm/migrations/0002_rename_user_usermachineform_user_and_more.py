# Generated by Django 4.1.5 on 2023-01-21 21:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RGForm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermachineform',
            old_name='user',
            new_name='User',
        ),
        migrations.RemoveField(
            model_name='usermachineform',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='usermachineform',
            name='machineName',
        ),
        migrations.RemoveField(
            model_name='usermachineform',
            name='usedInKms',
        ),
        migrations.AddField(
            model_name='usermachineform',
            name='Auftragsgeber',
            field=models.CharField(choices=[('Zilch', 'Zilch'), ('Horsch', 'Horsch'), ('Schmidl', 'Schmidl'), ('Dirmeier', 'Dirmeier'), ('Kopf', 'Kopf'), ('Maschinenring', 'Maschinenring')], default='Zilch', max_length=24),
        ),
        migrations.AddField(
            model_name='usermachineform',
            name='Betrieb',
            field=models.CharField(choices=[('neu', 'neu'), ('Brunner', 'Brunner'), ('Horsch', 'Horsch'), ('BG', 'BG'), ('Kopf', 'Kopf')], default='neu', max_length=24),
        ),
        migrations.AddField(
            model_name='usermachineform',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='usermachineform',
            name='Einheit',
            field=models.CharField(default='None', max_length=150),
        ),
        migrations.AddField(
            model_name='usermachineform',
            name='Fahrer',
            field=models.CharField(choices=[('neu', 'neu'), ('MD', 'MD'), ('MH', 'MH'), ('JS', 'JS'), ('TK', 'TK')], default='neu', max_length=24),
        ),
        migrations.AddField(
            model_name='usermachineform',
            name='LiterDiesel',
            field=models.CharField(default='Kein Schleper', max_length=150),
        ),
        migrations.AddField(
            model_name='usermachineform',
            name='Maschine',
            field=models.CharField(choices=[('Kein Maschine', 'Kein Schleper'), ('Pronto', 'Pronto'), ('Cruiser', 'Cruiser'), ('Tiger', 'Tiger'), ('Lemken Smaragt', 'Lemken Smaragt'), ('Komoststreuer', 'Komoststreuer'), ('Anhanger', 'Anhanger')], default='Kein Maschine', max_length=24),
        ),
        migrations.AddField(
            model_name='usermachineform',
            name='MaschineAnzahl',
            field=models.CharField(default='None', max_length=150),
        ),
        migrations.AddField(
            model_name='usermachineform',
            name='MaschineEnde',
            field=models.CharField(default='None', max_length=150),
        ),
        migrations.AddField(
            model_name='usermachineform',
            name='MaschineStart',
            field=models.CharField(default='None', max_length=150),
        ),
        migrations.AddField(
            model_name='usermachineform',
            name='Notizen',
            field=models.CharField(default='Kein Schleper', max_length=150),
        ),
        migrations.AddField(
            model_name='usermachineform',
            name='OrtDerTankung',
            field=models.CharField(choices=[('Kein Schleper', 'Kein Schleper'), ('6155R Stunden', '6155R Stunden'), ('6215R Studen', '6215R Studen')], default='Kein Schleper', max_length=24),
        ),
        migrations.AddField(
            model_name='usermachineform',
            name='Schlepper',
            field=models.CharField(choices=[('Kein Schleper', 'Kein Schleper'), ('6155R Stunden', '6155R Stunden'), ('6215R Studen', '6215R Studen')], default='Kein Schleper', max_length=24),
        ),
        migrations.AddField(
            model_name='usermachineform',
            name='SchlepperAnzahl',
            field=models.CharField(default='None', max_length=150),
        ),
        migrations.AddField(
            model_name='usermachineform',
            name='SchlepperEnde',
            field=models.CharField(default='None', max_length=150),
        ),
        migrations.AddField(
            model_name='usermachineform',
            name='SchlepperStart',
            field=models.CharField(default='None', max_length=150),
        ),
        migrations.AddField(
            model_name='usermachineform',
            name='Taetigkeit',
            field=models.CharField(choices=[('Kein Schleper', 'Kein Schleper'), ('6155R Stunden', '6155R Stunden'), ('6215R Studen', '6215R Studen')], default='Kein Schleper', max_length=24),
        ),
    ]
