# Generated by Django 4.1.5 on 2023-02-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RGForm', '0017_alter_usermachine_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermachine',
            name='DateTime',
            field=models.CharField(default='05-02-2023 14:33:37', max_length=60, verbose_name='System ZeitstempelDerEingabe'),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='Maschine',
            field=models.CharField(choices=[('None', '-----'), ('Keine Maschine', 'Keine Maschine'), ('Pronto', 'Pronto'), ('Cruiser', 'Cruiser'), ('Tiger', 'Tiger'), ('Lemken Smaragt', 'Lemken Smaragt'), ('Komoststreuer', 'Komoststreuer'), ('Anhanger', 'Anhanger')], default='None', max_length=24),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='MaschineAnzahl',
            field=models.CharField(default='0', max_length=150),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='MaschineEnde',
            field=models.CharField(default='0', max_length=150),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='MaschineLastRecord',
            field=models.CharField(default='0', max_length=150),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='MaschineStart',
            field=models.CharField(default='0', max_length=150),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='SchlepperAnzahl',
            field=models.CharField(default='0', max_length=150),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='SchlepperEnde',
            field=models.CharField(default='0', max_length=150),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='SchlepperLastRecord',
            field=models.CharField(default='0', max_length=150),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='SchlepperStart',
            field=models.CharField(default='0', max_length=150),
        ),
    ]