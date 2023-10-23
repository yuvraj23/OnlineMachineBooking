# Generated by Django 4.1.5 on 2023-02-04 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RGForm', '0008_alter_usermachine_date_alter_usermachine_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schlepper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Kein_Schleper', models.BigIntegerField(default=0)),
                ('Stunden_6155R', models.BigIntegerField(default=0)),
                ('Studen_6215R', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='machines',
            name='lastUpdateBy',
            field=models.CharField(default='None', max_length=150),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='Auftragsgeber',
            field=models.CharField(choices=[('None', '-----'), ('Zilch', 'Zilch'), ('Horsch', 'Horsch'), ('Schmidl', 'Schmidl'), ('Dirmeier', 'Dirmeier'), ('Kopf', 'Kopf'), ('Maschinenring', 'Maschinenring')], default='None', max_length=24),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='Betrieb',
            field=models.CharField(choices=[('None', '-----'), ('neu', 'neu'), ('Brunner', 'Brunner'), ('Horsch', 'Horsch'), ('BG', 'BG'), ('Kopf', 'Kopf')], default='None', max_length=24),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='Fahrer',
            field=models.CharField(choices=[('None', '-----'), ('neu', 'neu'), ('MD', 'MD'), ('MH', 'MH'), ('JS', 'JS'), ('TK', 'TK')], default='None', max_length=24),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='Maschine',
            field=models.CharField(choices=[('None', '-----'), ('Kein Maschine', 'Kein Schleper'), ('Pronto', 'Pronto'), ('Cruiser', 'Cruiser'), ('Tiger', 'Tiger'), ('Lemken Smaragt', 'Lemken Smaragt'), ('Komoststreuer', 'Komoststreuer'), ('Anhanger', 'Anhanger')], default='None', max_length=24),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='OrtDerTankung',
            field=models.CharField(choices=[('None', '-----'), ('Kein Schleper', 'Kein Schleper'), ('6155R Stunden', '6155R Stunden'), ('6215R Studen', '6215R Studen')], default='None', max_length=24),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='Schlepper',
            field=models.CharField(choices=[('None', '-----'), ('Kein Schleper', 'Kein Schleper'), ('6155R Stunden', '6155R Stunden'), ('6215R Studen', '6215R Studen')], default='None', max_length=24),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='Taetigkeit',
            field=models.CharField(choices=[('None', '-----'), ('Kein Schleper', 'Kein Schleper'), ('6155R Stunden', '6155R Stunden'), ('6215R Studen', '6215R Studen')], default='None', max_length=24),
        ),
    ]