from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError




# Create your models here.



class DropDownMenu(models.Model):
    drop_down_name=models.CharField(max_length=40,null=True)
    list_of_choice = models.JSONField()
    def clean(self):
        self.list_of_choice=list(set(self.list_of_choice))
        if isinstance(type(self.list_of_choice), list):
            raise ValidationError("Dates are incorrect")


import datetime
from datetime import datetime

def gettime():
    import datetime
    now = datetime.datetime.now().strftime('%H:%M:%S')
    return now

def getDate():
    import datetime
    year=str(datetime.date.today().year)
    mon=str(datetime.date.today().month)
    day=str(datetime.date.today().day)

    if int(mon)<10:
        mon="0"+mon
    if int(day)<10:
        day="0"+day
    date=day+"-"+mon+"-"+year

    return date

def getDateAndTime():
    date=getDate()
    currentTime = str(gettime())
    res=date +" "+currentTime
    return res

class UserMachine(models.Model):
    User =models.ForeignKey(User, on_delete=models.CASCADE,default=None,blank=True,null=True,verbose_name="Benutzer")
    Date =models.CharField(max_length=24,default=None,verbose_name="Datum")
    Auftragsgeber =models.CharField(max_length=24, default='None')
    Betrieb =models.CharField(max_length=24, default='None')
    Fahrer =models.CharField(max_length=24, default='None')
    Schlepper =models.CharField(max_length=24, default='None')
    SchlepperLastRecord =models.CharField(max_length=150,default='0')
    SchlepperUnit =models.CharField(max_length=50,default='None')
    SchlepperStart =models.CharField(max_length=150,default='0',)
    SchlepperEnde =models.CharField(max_length=150,default='0')
    SchlepperAnzahl =models.CharField(max_length=150,default='0')
    OrtDerTankung =models.CharField(max_length=24, default='',verbose_name="Ort der Tankung")
    LiterDiesel =models.CharField(max_length=100,default='0',verbose_name="Liter Diesel")
    Maschine =models.CharField(max_length=24, default='None')
    MaschineLastRecord =models.CharField(max_length=150,default='0')
    MaschineUnit =models.CharField(max_length=50,default='None')
    MaschineStart =models.CharField(max_length=150,default='0')
    MaschineEnde =models.CharField(max_length=150,default='0')
    MaschineAnzahl =models.CharField(max_length=150,default='0')
    Taetigkeit =models.CharField(max_length=24,default='0')

    Notizen =models.TextField(max_length=150,default='')
    DateTime=models.CharField(max_length=60,default=getDateAndTime(),verbose_name="ZeitstempelDerEingabe")
    created_at=models.DateField(auto_now_add=True,blank=True,null=True)



class Machines(models.Model):
    Keine_Maschine=models.FloatField(default=0)
    Pronto=models.FloatField(default=0)
    Cruiser=models.FloatField(default=0)
    Lemken_Smaragd=models.FloatField(default=0)
    Komoststreuer_1=models.BigIntegerField(default=0)
    Presse=models.BigIntegerField(default=0)
    Tiger=models.FloatField(default=0)
    Komoststreuer_2=models.BigIntegerField(default=0)
    Pflug_5_Schar=models.FloatField(default=0)
    lastUpdateBy=models.CharField(max_length=150,default='None')

class Schlepper(models.Model):
    Kein_Schleper=models.FloatField(default=0)
    SAD_SI_185=models.FloatField(default=0)
    SAD_SI_602=models.FloatField(default=0)
    SAD_SI_601=models.FloatField(default=0)

class UnitTable(models.Model):
    unit_for=models.CharField(max_length=40,null=True)
    units = models.JSONField()

class UserProfile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE,default=None,blank=True,null=True,verbose_name="user_name")
    password=models.CharField(max_length=100, default='None',verbose_name="password")
    driver=models.CharField(max_length=100, default='None',verbose_name="driver")


# When any User instance created, Profile object instance is created automatically linked by User
from django.dispatch import receiver
from django.db.models.signals import post_save
@receiver(post_save, sender = User)
def user_is_created(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user= instance)










