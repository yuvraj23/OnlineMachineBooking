from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect,HttpResponse,render,get_object_or_404
from .forms import SignUpform,Loginform,UserMachineForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import UserMachine,Machines,Schlepper,DropDownMenu,UnitTable,UserProfile
from django.contrib.auth.decorators import login_required


try:
    machineUnits=get_object_or_404(UnitTable,unit_for="MachineUnits").units
except:
    machineUnits={"Pronto":"Hektar","Cruiser":"Hektar","Tiger":"Hektar","Lemken Smaragt":"Hektar","Komoststreuer":"Fuhren","Anhänger":"Fuhren"}


try:
    schlepperUnits=get_object_or_404(UnitTable,unit_for="SchlepperUnits").units
except:
    schlepperUnits={"6155R Stunden":"Std","6215R Stunden":"Std"}

displayMachineFiels={'Komoststreuer 1':'Komoststreuer 1','Lemken Smaragt':'Lemken Smaragt','Pflug 5-Schar':'Pflug 5-Schar'}


def index(request):
    data_save=request.session.get('data_save')
    request.session['data_save']=False
    return render(request,'RGFormTemplates/html/home.html',{'data_save':data_save})

def user_login(request):

    if not request.user.is_authenticated:
        if request.method == "POST":
            form=Loginform(request=request,data=request.POST)

            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']

                user=authenticate(username=uname,password=upass)
                if user is not None:

                    login(request,user)

                    return HttpResponseRedirect("/")
            form=Loginform()
            valid=False
            return render(request,'RGFormTemplates/html/login.html',{'form':form,'valid':valid})
        else:
            form=Loginform()
            valid=True
            return render(request,'RGFormTemplates/html/login.html',{'form':form,'valid':valid})
    else:
        valid=True
        return HttpResponseRedirect("/",{'valid':valid})



def user_logout(request):
    logout(request)
    return render(request,'RGFormTemplates/html/logout.html')

def user_register(request):
    if request.method=="POST":
        form=SignUpform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignUpform()
    return render(request,'RGFormTemplates/html/register.html',{'form':form})

def showUserHistory(request):
    if request.user.is_authenticated:
       history=UserMachine.objects.filter(User=request.user)
       return render(request,'RGFormTemplates/html/history.html',{'history':history})
    else:
        return render(request,'RGFormTemplates/html/home.html')

@login_required(login_url='user_login')
def addDataInForm(request):

    Maschine_Choices = {
    'Kein Maschine': 'Kein_Schleper',
    'Pronto':"Pronto",
    'Cruiser':"Cruiser",
    'Tiger': 'Tiger',
    'Lemken Smaragt':"Lemken_Smaragt",
    'Komoststreuer':"Komoststreuer",
    'Anhanger':"Anhanger",
    }
    data_save=False

    if request.method=="POST":
        form=UserMachineForm(request.POST)
        print("checking form : ",form.data)
        
        if form.is_valid():
           
            user=get_object_or_404(User,username=request.user.username)

            form=form.save(commit=False)
            userDate=str(form.Date).split("-")
            form.Date=userDate[2]+"-"+userDate[1]+"-"+userDate[0]

            ############################# for maschine ##########################

            machineData=form.Maschine
            if machineData!="Keine Maschine":
                machineUpdatedDistance=form.MaschineAnzahl
                machineUpdatedDistance=float(machineUpdatedDistance)
                machine=get_object_or_404(Machines,id=1)
                if machineData == "Pronto":
                    print(float(machine.Pronto),"  ===  ",form.MaschineLastRecord, "  , ,, ",machineUpdatedDistance,"     => ",form.MaschineLastRecord==float(machine.Pronto))
                    if float(machine.Pronto) != float(form.MaschineLastRecord):
                        print(float(machine.Pronto),"  ===  ",form.MaschineLastRecord,"     => ",form.MaschineLastRecord==float(machine.Pronto))
                        form.MaschineLastRecord=float(machine.Pronto)
                        form.MaschineStart=float(machine.Pronto)
                        form.MaschineEnde=float(form.MaschineStart)+float(form.MaschineAnzahl)

                    machine.Pronto= float(machine.Pronto)+machineUpdatedDistance
                elif machineData =="Keine Maschine":
                    if float(machine.Keine_Maschine) != form.MaschineLastRecord:
                        form.MaschineLastRecord=float(machine.Keine_Maschine)
                        form.MaschineStart=float(machine.Keine_Maschine)
                        form.MaschineEnde=float(form.MaschineStart)+float(form.MaschineAnzahl)

                    machine.Keine_Maschine=float(machine.Keine_Maschine)+machineUpdatedDistance
                elif machineData == "Cruiser":
                    if float(machine.Cruiser) != form.MaschineLastRecord:
                        form.MaschineLastRecord=float(machine.Cruiser)
                        form.MaschineStart=float(machine.Cruiser)
                        form.MaschineEnde=float(form.MaschineStart)+float(form.MaschineAnzahl)

                    machine.Cruiser=float(machine.Cruiser)+machineUpdatedDistance
                elif machineData == "Tiger":
                    if float(machine.Tiger) != form.MaschineLastRecord:
                        form.MaschineLastRecord=float(machine.Tiger)
                        form.MaschineStart=float(machine.Tiger)
                        form.MaschineEnde=float(form.MaschineStart)+float(form.MaschineAnzahl)

                    machine.Tiger=float(machine.Tiger)+machineUpdatedDistance
                elif machineData == "Lemken Smaragd":
                    if float(machine.Lemken_Smaragd) != form.MaschineLastRecord:
                        form.MaschineLastRecord=float(machine.Lemken_Smaragd)
                        form.MaschineStart=float(machine.Lemken_Smaragd)
                        form.MaschineEnde=float(form.MaschineStart)+float(form.MaschineAnzahl)

                    machine.Lemken_Smaragd=float(machine.Lemken_Smaragd)+machineUpdatedDistance
                elif machineData == "Komoststreuer 1":
                    if float(machine.Komoststreuer_1) != form.MaschineLastRecord:
                        form.MaschineLastRecord=float(machine.Komoststreuer_1)
                        form.MaschineStart=float(machine.Komoststreuer_1)
                        form.MaschineEnde=float(form.MaschineStart)+float(form.MaschineAnzahl)

                    machine.Komoststreuer_1=float(machine.Komoststreuer_1)+machineUpdatedDistance
                elif machineData == "Komoststreuer 2":
                    if float(machine.Komoststreuer_2) != form.MaschineLastRecord:
                        form.MaschineLastRecord=float(machine.Komoststreuer_2)
                        form.MaschineStart=float(machine.Komoststreuer_2)
                        form.MaschineEnde=float(form.MaschineStart)+float(form.MaschineAnzahl)

                    machine.Komoststreuer_2=float(machine.Komoststreuer_2)+machineUpdatedDistance
                elif machineData == "Pflug 5-Schar":
                    if float(machine.Pflug_5_Schar) != form.MaschineLastRecord:
                        form.MaschineLastRecord=float(machine.Pflug_5_Schar)
                        form.MaschineStart=float(machine.Pflug_5_Schar)
                        form.MaschineEnde=float(form.MaschineStart)+float(form.MaschineAnzahl)

                    machine.Pflug_5_Schar=float(machine.Pflug_5_Schar)+machineUpdatedDistance
                elif machineData == "Presse":
                    if float(machine.Presse) != form.MaschineLastRecord:
                        form.MaschineLastRecord=float(machine.Presse)
                        form.MaschineStart=float(machine.Presse)
                        form.MaschineEnde=float(form.MaschineStart)+float(form.MaschineAnzahl)

                    machine.Presse=float(machine.Presse)+machineUpdatedDistance
                machine.save()
            else:
                form.MaschineLastRecord="None"
                form.MaschineStart="None"
                form.MaschineEnde="None"
                form.MaschineAnzahl="None"

            ############################# for schlepper ##########################
            schlepperData=form.Schlepper
            print(form)
            if schlepperData!="Keine Schlepper":
                schlepperUpdatedDistance=form.SchlepperAnzahl
                schlepperUpdatedDistance=float(schlepperUpdatedDistance)
                schlepper=get_object_or_404(Schlepper,id=1)
                if schlepperData == "SAD SI 602":

                    if float(schlepper.SAD_SI_602) != form.SchlepperLastRecord:
                        form.SchlepperLastRecord=float(schlepper.SAD_SI_602)
                        form.SchlepperStart=float(schlepper.SAD_SI_602)
                        form.SchlepperEnde=float(form.SchlepperStart)+float(form.SchlepperAnzahl)

                    schlepper.SAD_SI_602=float(schlepper.SAD_SI_602)+schlepperUpdatedDistance
                elif schlepperData =="SAD SI 185":

                    if float(schlepper.SAD_SI_602) != form.SchlepperLastRecord:
                        form.SchlepperLastRecord=float(schlepper.SAD_SI_602)
                        form.SchlepperStart=float(schlepper.SAD_SI_602)
                        form.SchlepperEnde=float(form.SchlepperStart)+float(form.SchlepperAnzahl)

                    schlepper.SAD_SI_185=float(schlepper.SAD_SI_185)+schlepperUpdatedDistance
                elif schlepperData =="SAD SI 601":

                    if float(schlepper.SAD_SI_602) != form.SchlepperLastRecord:
                        form.SchlepperLastRecord=float(schlepper.SAD_SI_602)
                        form.SchlepperStart=float(schlepper.SAD_SI_602)
                        form.SchlepperEnde=float(form.SchlepperStart)+float(form.SchlepperAnzahl)

                    schlepper.SAD_SI_601=float(schlepper.SAD_SI_601)+schlepperUpdatedDistance

                schlepper.save()
            else:
                form.SchlepperLastRecord="None"
                form.SchlepperStart="None"
                form.id_SchlepperEnde="None"
                form.SchlepperAnzahl="None"

            form.User =user


            form.SchlepperUnit=schlepperUnits.get(schlepperData,"None")
            form.MaschineUnit=machineUnits.get(machineData,"None")

            form.save()
            data_save=True
            request.session['data_save']=data_save
            return HttpResponseRedirect("/",{'data_save':data_save})
    else:
        user=get_object_or_404(User,username=request.user.username)
        machine_km=get_object_or_404(Machines,id=1)
        schlepper_km=get_object_or_404(Schlepper,id=1)

        dict_machine={"Keine Maschine":machine_km.Keine_Maschine,"Pronto":machine_km.Pronto,
        "Cruiser":machine_km.Cruiser,"Lemken Smaragd":machine_km.Lemken_Smaragd,
        "Komoststreuer 1":machine_km.Komoststreuer_1, "Komoststreuer 2":machine_km.Komoststreuer_2,
        "Pflug 5-Schar":machine_km.Pflug_5_Schar,"Presse":machine_km.Presse,'Tiger':machine_km.Tiger}


        dict_schlepper={"SAD SI 602":schlepper_km.SAD_SI_602,"SAD SI 185":schlepper_km.SAD_SI_185,"SAD SI 601":schlepper_km.SAD_SI_601}

        form = UserMachineForm(initial={"User":user})
        driver_lst=UserProfile.objects.all()
        driverName="None"
        for d in driver_lst:

            if str(d.user)==str(request.user.username):
                driverName=d.driver
                print("*"*10 ,driverName,"*"*10 )
                break
        form = UserMachineForm(initial={"Fahrer":driverName})

        return render(request,'RGFormTemplates/html/displayFrom.html',{'form':form,"dict_machine":dict_machine,"dict_schlepper":dict_schlepper,"machineUnits":machineUnits,"schlepperUnits":schlepperUnits,'displayMachineFiels':displayMachineFiels})


import datetime
def getDate():
    now=datetime.datetime.now()
    return now.strftime("%Y-%m-%d")


def Impressum(request):
    return render(request,'RGFormTemplates/html/Impressum.html')

def Datenschutz(request):
    return render(request,'RGFormTemplates/html/Datenschutz.html')

def Kontakt(request):
    return render(request,'RGFormTemplates/html/Kontakt.html')








