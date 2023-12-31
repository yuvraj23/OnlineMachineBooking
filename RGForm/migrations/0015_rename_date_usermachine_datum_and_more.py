# Generated by Django 4.1.5 on 2023-02-05 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RGForm', '0014_alter_usermachine_datetime_alter_usermachine_notizen_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermachine',
            old_name='Date',
            new_name='Datum',
        ),
        migrations.RenameField(
            model_name='usermachine',
            old_name='MaschineUnit',
            new_name='MaschineEinheit',
        ),
        migrations.RenameField(
            model_name='usermachine',
            old_name='SchlepperUnit',
            new_name='SchlepperEinheit',
        ),
        migrations.RemoveField(
            model_name='usermachine',
            name='DateTime',
        ),
        migrations.RemoveField(
            model_name='usermachine',
            name='MaschineAnzahl',
        ),
        migrations.RemoveField(
            model_name='usermachine',
            name='MaschineLastRecord',
        ),
        migrations.RemoveField(
            model_name='usermachine',
            name='MaschineStart',
        ),
        migrations.RemoveField(
            model_name='usermachine',
            name='SchlepperAnzahl',
        ),
        migrations.RemoveField(
            model_name='usermachine',
            name='SchlepperLastRecord',
        ),
        migrations.RemoveField(
            model_name='usermachine',
            name='SchlepperStart',
        ),
        migrations.AddField(
            model_name='usermachine',
            name='MaschineAnfang',
            field=models.CharField(default='None', max_length=150, verbose_name='Anfang'),
        ),
        migrations.AddField(
            model_name='usermachine',
            name='MaschineAnfangEndeZuletzt',
            field=models.CharField(default='None', max_length=150, verbose_name='Anfang/Ende Zuletzt'),
        ),
        migrations.AddField(
            model_name='usermachine',
            name='MaschineVerbrauch',
            field=models.CharField(default='None', max_length=150, verbose_name='Verbrauch'),
        ),
        migrations.AddField(
            model_name='usermachine',
            name='SchlepperAnfang',
            field=models.CharField(default='None', max_length=150, verbose_name='Anfang'),
        ),
        migrations.AddField(
            model_name='usermachine',
            name='SchlepperAnfangEndeZuletzt',
            field=models.CharField(default='None', max_length=150, verbose_name='Anfang/Ende Zuletzt'),
        ),
        migrations.AddField(
            model_name='usermachine',
            name='SchlepperVerbrauch',
            field=models.CharField(default='None', max_length=150, verbose_name='Verbrauch'),
        ),
        migrations.AddField(
            model_name='usermachine',
            name='ZeitstempelDerEingabe',
            field=models.CharField(default='05-02-2023 13:21:35', max_length=60, verbose_name='Zeitstempel der Eingabe'),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='MaschineEnde',
            field=models.CharField(default='None', max_length=150, verbose_name='Ende'),
        ),
        migrations.AlterField(
            model_name='usermachine',
            name='SchlepperEnde',
            field=models.CharField(default='None', max_length=150, verbose_name='Ende'),
        ),
    ]
