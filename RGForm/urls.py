from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('user_register/', views.user_register, name='user_register'),
    path('showUserHistory/', views.showUserHistory, name='showUserHistory'),
    path('addDataInForm/', views.addDataInForm, name='addDataInForm'),

    path('Impressum/', views.Impressum, name='Impressum'),
    path('Datenschutz/', views.Datenschutz, name='Datenschutz'),
    path('Kontakt/', views.Kontakt, name='Kontakt'),
    path(r'^.*/$', views.index, name='index'),

]


from django.contrib import admin
admin.site.site_header = 'MGS Fahrtenbuch Database'     # default: "Django Administration"
admin.site.index_title = 'MGS Fahrtenbuch v1.0 made with love in Bavaria by Rahul Sarwal'                # default: "Site administration"
admin.site.site_title = 'MGS Fahrtenbuch'