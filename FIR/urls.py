from django.contrib import admin
from django.urls import path
from FIR import views

urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contact",views.contact, name='contact'),
    path("filefir",views.filefir, name="filefir"),
    path("filefir1",views.filefir1, name="filefir1"),
    path("categories",views.categories, name="categories"),
    path("track_status",views.track_status, name="track_status"),
    path("ngo",views.ngo, name="ngo"), 
    path("emergency",views.emergency, name="emergency"),
    path("quick",views.quick, name="quick"),
    path("download_fir",views.download_fir, name="download_fir")
]