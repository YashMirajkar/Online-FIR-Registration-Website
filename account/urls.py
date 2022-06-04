from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path("register",views.register, name='register'),
    path("login",views.login,name='login'),
    path("logout",views.logout,name='logout'),
    path("viewfir/<str:username>",views.viewfir,name='viewfir'),
    path("home/<str:username>",views.home,name='home'),
    path("loadfir/<str:pk>/<str:username>",views.loadfir,name='loadfir'),
    path("contact/<str:pk>/<str:username>",views.contact,name='contact'),
    path("updatestatus/<str:pk>/<str:username>",views.updatestatus,name='updatestatus'),
    path("profile/<str:username>",views.profile, name="profile"),
    path("printfir/<str:pk>/<str:username>",views.printfir,name='printfir')
    
]