from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from .models import UserMachine
from django.utils.translation import gettext,gettext_lazy as _
from django.shortcuts import get_object_or_404
from .models import UserMachine,Machines,Schlepper,DropDownMenu
from django.contrib.auth import authenticate,login,logout


class SignUpform(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        help_texts = {
            'username': None,
            'email': None
        }
        widgets={
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'})
        }


def getDate():
    import datetime
    year=str(datetime.date.today().year)
    mon=str(datetime.date.today().month)
    day=str(datetime.date.today().day)

    if int(mon)<10:
        mon="0"+mon
    if int(day)<10:
        day="0"+day

    date=year+"-"+mon+"-"+day
    print("date is :",date);

    return date

def getChoice(dropdown):
        dd=dropdown
        dropdown=get_object_or_404(DropDownMenu,drop_down_name=dropdown)
        len_of_dropdown=len(dropdown.list_of_choice)+1
        if dropdown!=None:
            choiceLst=[(0,0)*2]*len_of_dropdown


            for ch in dropdown.list_of_choice:
                keyVal=ch.split("_")
                ind=int(keyVal[0])-1
                key=keyVal[1].strip()
                val=keyVal[1].strip()
                choiceLst[ind]=(key,val)
        choiceLst.pop()
        if(dd=="Schlepper_Choices"):
            choiceLst.insert(0,("Kein Schlepper","----------"))
        elif (dd=="Maschine_Choices"):
            choiceLst.insert(0,("Keine Maschine","----------"))
        else:
            choiceLst.insert(0,("None","----------"))

        return choiceLst

class UserMachineForm(forms.ModelForm):
    getDate()
    class Meta:
        model=UserMachine
        fields='__all__'
        exclude = ('DateTime','SchlepperUnit','MaschineUnit')

        User = forms.CharField(max_length=100)
        Auftragsgeber = forms.CharField(max_length=100)
        Date = forms.CharField(max_length=100)
        Betrieb = forms.CharField(max_length=100)
        Fahrer = forms.CharField(max_length=100)

        Schlepper = forms.CharField(max_length=100)
        SchlepperLastRecord = forms.IntegerField()
        SchlepperStart = forms.IntegerField()
        SchlepperEnde = forms.IntegerField()
        SchlepperAnzahl = forms.IntegerField()

        Maschine = forms.CharField(max_length=100)
        MaschineLastRecord = forms.IntegerField()
        MaschineStart = forms.IntegerField()
        MaschineEnde = forms.IntegerField()
        MaschineAnzahl = forms.IntegerField()

        Taetigkeit = forms.CharField(max_length=100)
        OrtDerTankung = forms.CharField(max_length=100)
        LiterDiesel = forms.CharField(max_length=100)
        Notizen = forms.CharField(max_length=100)
        DateTime = forms.CharField(max_length=100)
        SchlepperUnit = forms.CharField(max_length=100)
        MaschineUnit = forms.CharField(max_length=100)

        widgets={
        'Auftragsgeber':forms.Select(choices=getChoice("Auftragsgeber_Choices"),attrs={'class':'form-control'}),
        'User':forms.HiddenInput(attrs={'class':'form-control'}),
        'Date':forms.DateInput(attrs={'class':'form-control','type': 'date','value':getDate(),'onChange':'dateValidation()'}),
        'Time':forms.TextInput(attrs={'class':'form-control','type': 'time'}),
        'Betrieb':forms.Select(choices=getChoice("Betrieb_Choices"),attrs={'class':'form-control'}),
        'Fahrer':forms.Select(choices=getChoice("Fahrer_Choices"),attrs={'class':'form-control'}),

        'Schlepper':forms.Select(choices=getChoice("Schlepper_Choices"),attrs={'class':'form-control','onChange':'calculateSchlepperKm();setSchlUnit()'}),

        'SchlepperLastRecord':forms.TextInput(attrs={'class':'form-control','readonly':'true','type':'number'}),
        'SchlepperStart':forms.TextInput(attrs={'class':'form-control','onChange':'validatestartSchlepperValue()','type':'number'}),
        'SchlepperEnde':forms.TextInput(attrs={'class':'form-control','type':'number','onChange':'validateEndSchlepperValue();calculateSchlepperDiff()','onmouseover':'over("id_SchlepperEnde")','onmousout':'out("id_SchlepperEnde")'}),
        'SchlepperAnzahl':forms.TextInput(attrs={'class':'form-control','type':'number','readonly':'true'}),

        'Maschine':forms.Select(choices=getChoice("Maschine_Choices"),attrs={'class':'form-control','onChange':'calculateMachineKm();setMachUnit()'}),

        'MaschineLastRecord':forms.TextInput(attrs={'class':'form-control','type':'number','readonly':'true'}),
        'MaschineStart':forms.TextInput(attrs={'class':'form-control','type':'number','onChange':'validateStartValue()'}),
        'MaschineEnde':forms.TextInput(attrs={'class':'form-control','type':'number','onChange':'validateEndValue();calculateDiff()','onmouseover':'over("id_MaschineEnde")','onmouseout':'out("id_MaschineEnde")'}),
        'MaschineAnzahl':forms.TextInput(attrs={'class':'form-control','type':'number','readonly':'true'}),

        'Taetigkeit':forms.Select(choices=getChoice("Taetigkeit_Choices"),attrs={'class':'form-control'}),
        'OrtDerTankung':forms.Select(choices=getChoice("OrtDerTankung_Choices"),attrs={'class':'form-control','onChange':'blockField("id_OrtDerTankung")'}),
        'LiterDiesel':forms.TextInput(attrs={'class':'form-control','readonly':'true','onmouseover':'over("id_LiterDiesel")','onmouseout':'out("id_LiterDiesel")','onChange':'integerCheck()','type':'number'}),
        'Notizen':forms.Textarea(attrs={'class':'form-control','onmouseover':'over("id_Notizen")','onmouseout':'out("id_Notizen")','rows':3, 'cols': 5}),
        'DateTime':forms.TextInput(attrs={'type': 'hidden'}),
        'SchlepperUnit':forms.TextInput(attrs={'type': 'hidden'}),
        'MaschineUnit':forms.TextInput(attrs={'type': 'hidden'})
        }
        labels = {
             'Date': 'Datum',
             'User':'Benutzer',
             'SchlepperLastRecord':'Anfang/Ende Zuletzt (Abweichungen in Notizen eintragen)',
             'SchlepperStart':'Anfang',
             'SchlepperEnde':'Ende',
             'SchlepperAnzahl':'Verbrauch',

             'MaschineLastRecord':'Anfang/Ende Zuletzt (Abweichungen in Notizen eintragen)',
             'MaschineStart':'Anfang',
             'MaschineEnde':'Ende',
             'MaschineAnzahl':'Verbrauch',
             'LiterDiesel':'Liter Diesel',
             'OrtDerTankung':'Ort der Tankung',
             'Notizen':'Notizen',
             'Betrieb':'Betrieb (Optional)',
             'Taetigkeit':'Tätigkeit (Optional)'

        }




class Loginform(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_("Password"),strip=False,widget=forms.TextInput(attrs={'autocomplete':'current-password','class':'form-control'}))





