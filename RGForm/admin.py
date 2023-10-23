from django.contrib import admin
from .models import UserMachine,Machines,Schlepper,DropDownMenu,UnitTable,UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.http import HttpResponse
import csv
import pandas as pd
import xlwt
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags,format_html

# Register your models here.

new_german_cloumn_name={'User': 'user_name', 'Date': 'date', 'Auftragsgeber': 'Auftragsgeber_modified_one', 'Betrieb': 'Betrieb_testing', 'Fahrer': 'Fahrer', 'Schlepper': 'Schlepper', 'SchlepperUnit': 'SchlepperUnit', 'OrtDerTankung': 'OrtDerTankung', 'Maschine': 'Maschine', 'MaschineUnit': 'MaschineUnit', 'Taetigkeit': 'Taetigkeit', 'Notizen': 'Notizen', 'DateTime': 'DateTime', 'created_at': 'created_at'}

def download_csv(modeladmin, request, queryset):

    if not request.user.is_staff:
        raise PermissionDenied
    opts = queryset.model._meta
    model = queryset.model
    response = HttpResponse(content_type='text/csv')
    # force download.
    response['Content-Disposition'] = 'attachment;filename=export.xls'
    # the csv writer
    writer = csv.writer(response)
    field_names = [field.name for field in opts.fields]
    # Write a first row with header information
    writer.writerow(field_names)
    # Write data rows
    for obj in queryset:

        for field in field_names:
            print(getattr(obj, field),end=" ")
        print()

        writer.writerow([getattr(obj, field) for field in field_names])
    return response
download_csv.short_description = "Download Data as csv"

def download_excel(modeladmin, request, queryset):
    from io import BytesIO
    opts = queryset.model._meta
    columns = [field.name for field in opts.fields if field.name!="id" ]
    data={}
    for col in columns:
        data[col]=[]
    listOfNums=["SchlepperLastRecord","SchlepperStart","SchlepperEnde","SchlepperAnzahl","MaschineLastRecord","MaschineStart","MaschineEnde","MaschineAnzahl","LiterDiesel"]
    for obj in queryset:
        for field in range(len(columns)):
            if columns[field] in listOfNums:
                val=getattr(obj, columns[field])
                if getattr(obj, columns[field]) == "None":
                    val="0.0"
                valueStr=str(val)
                if ',' in valueStr:
                    valueStr.replace(',','.')

                data[columns[field]].append(float(valueStr))
            else:
                data[columns[field]].append(str(getattr(obj, columns[field])))

    df = pd.DataFrame(data)
    for col in new_german_cloumn_name:
        df.rename(columns = {col:new_german_cloumn_name.get(col,col)}, inplace = True)


    # from here you need add new column name like this
    df.rename(columns = {'User':'user_name'}, inplace = True)


    print(df)
    with BytesIO() as b:
        # Use the StringIO object as the filehandle.
        writer = pd.ExcelWriter(b, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1')
        writer.save()
        # Set up the Http response.
        filename = 'database_Result_Set.xlsx'
        response = HttpResponse(
            b.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response
download_excel.short_description = "Export data as excel"


@admin.register(UserMachine)
class UserMachineAdmin(admin.ModelAdmin):
    from django.db import models
    from django.forms import TextInput, Textarea
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'2000'})},
        models.TextField: {'widget': Textarea(attrs={'rows':400, 'cols':4000})},
    }
    list_display=['view_data','Date',"DateTime",'User','Auftragsgeber','Betrieb','Fahrer','Schlepper','SchlepperStart','SchlepperEnde','SchlepperUnit',
   'SchlepperLastRecord' ,'SchlepperAnzahl','Maschine','MaschineStart','MaschineEnde','MaschineUnit','MaschineLastRecord','MaschineAnzahl','Taetigkeit'
    ,'OrtDerTankung','LiterDiesel','Notizen']
    list_filter = ('created_at','User','Fahrer', 'Schlepper','Maschine')

    actions=[download_excel,]
   

    def view_data(self,obj):
          return format_html("<button type='button'  style='background-color: #4CAF50;  border: none; color: white; padding: 8px 10px;border-radius:10px; box-shadow: 0px 0px 2px 2px rgb(0,0,0); text-align: center; text-decoration: none; display: inline-block; font-size: 12px;'>Edit</button>")


@admin.register(Machines)
class MachineAdmin(admin.ModelAdmin):
    list_display=['view_data',"Keine_Maschine","Pronto","Cruiser","Lemken_Smaragd","Komoststreuer_1", "Komoststreuer_2", "Pflug_5_Schar", "Presse","Tiger"]
    def view_data(self,obj):
          return format_html("<button type='button'  style='background-color: #4CAF50;  border: none; color: white; padding: 8px 10px;border-radius:10px; box-shadow: 0px 0px 2px 2px rgb(0,0,0); text-align: center; text-decoration: none; display: inline-block; font-size: 12px;'>Edit</button>")

@admin.register(Schlepper)
class SchlepperAdmin(admin.ModelAdmin):
    list_display=['view_data',"Kein_Schleper","SAD_SI_185","SAD_SI_602","SAD_SI_601"]
    def view_data(self,obj):
          return format_html("<button type='button'  style='background-color: #4CAF50;  border: none; color: white; padding: 8px 10px;border-radius:10px; box-shadow: 0px 0px 2px 2px rgb(0,0,0); text-align: center; text-decoration: none; display: inline-block; font-size: 12px;'>Edit</button>")

@admin.register(DropDownMenu)
class DropDownMenuAdmin(admin.ModelAdmin):
    list_display=['view_data',"drop_down_name","list_of_choice"]
    def view_data(self,obj):
          return format_html("<button type='button'  style='background-color: #4CAF50;  border: none; color: white; padding: 8px 10px;border-radius:10px; box-shadow: 0px 0px 2px 2px rgb(0,0,0); text-align: center; text-decoration: none; display: inline-block; font-size: 12px;'>Edit</button>")

@admin.register(UnitTable)
class UnitTableAdmin(admin.ModelAdmin):
    list_display=['view_data',"unit_for","units"]
    def view_data(self,obj):
        return format_html("<button type='button'  style='background-color: #4CAF50;  border: none; color: white; padding: 8px 10px;border-radius:10px; box-shadow: 0px 0px 2px 2px rgb(0,0,0); text-align: center; text-decoration: none; display: inline-block; font-size: 12px;'>Edit</button>")

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user','password','driver']


class UserAdmin(AuthUserAdmin):
    actions = ['activate_user','deactivate_user',"send_user_creation_mail"]

    def activate_user(self, request, queryset):
        queryset.update(is_active=True)

    def deactivate_user(self, request, queryset):
        queryset.update(is_active=False)

    def send_user_creation_mail(self, request, queryset):
        book={}

        pass_lst=UserProfile.objects.all()
        for p in pass_lst:
            book[p.user.username]=p.password

        for obj in queryset:

            email=obj.email
            user=obj.first_name+" "+obj.last_name
            if(len(user)<3):
                user=obj.username

            print(book,"  ",obj.username)
            if(book.get(str(obj.username),None) is not None):

                    password=book.get(obj.username,"-")
                    context ={
                    "title":"Password for MGS Fahrtenbuch",
                    "content":"-----------------------------"
                    }
                    html_content =f"""
                        <!DOCTYPE html>
                        <html>
                        <head>

                        <style>
                        .card &&&
                        box-shadow: 0 4px 8px 0 rgba(100, 100, 100, 0.2);
                        font-family: arial;
                        |||

                        .title &&&
                        color: grey;
                        font-size: 18px;
                        |||

                        a:hover, a:hover &&&
                        opacity: 0.7;
                        |||

                        </style>
                        </head>
                        <body>

                        <h2 style="">{user} Ihre Login Daten:</h2>

                        <div class="card">
                        <p>Website URL : <a href="https://form.mgs-fahrtenbuch.de">form.mgs-fahrtenbuch.de</a></p>
                        <p>Benutzer : {obj.username} </p>
                        <p>Passwort : {password}</p>
                        <br>
                        <p>Freundliche Grüße </p>
                        <p>Ihre MGS </p> <br>
                        </div>

                        </body>
                        </html>

                    """
                    html_content=html_content.replace("&&&","{").replace("|||","}")
                    text_content = strip_tags(html_content)
                    email = EmailMultiAlternatives(
                        "Willkommen bei MGS Fahrtenbuch - Ihre Login Daten!! ",
                        text_content,
                        settings.EMAIL_HOST_USER ,
                        [email,'mgsfahrtenbuch@gmail.com']
                    )
                    email.attach_alternative(html_content, 'text/html')
                    from django.contrib import messages
                    messages.add_message(request, messages.INFO, 'Email sended successfully')
                    email.send()

    def view_data(self,obj):
        return format_html("<button type='button' style='background-color: #4CAF50; border: none; color: white; padding: 8px 10px; text-align: center; text-decoration: none; display: inline-block; font-size: 12px;'>Edit</button>")




    activate_user.short_description = "Activate selected users"
    deactivate_user.short_description = "Deactivate selected users"
    send_user_creation_mail.short_description="Send User Account Activation mail"
admin.site.unregister(User)
admin.site.register(User, UserAdmin)



