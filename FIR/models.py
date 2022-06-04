from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email.policy import default
import os
from django.db import models
import datetime
from django.contrib.auth.models import User

class Police_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pincode = models.IntegerField()
    Police_Station = models.CharField(max_length=50)

class FirModel(models.Model):
    request_no=models.IntegerField(primary_key=True)
    crime_type=models.CharField(max_length=150)
    fir_status=models.CharField(max_length=150)
    fir_no=models.IntegerField()
    password=models.CharField(max_length=150)
    comments=models.TextField(max_length=150,default=NULL)
    police_id=models.IntegerField(default=NULL)
    class Meta:
        db_table="Main_Table"

class Complainant(models.Model):
    id=models.AutoField(primary_key=True)
    #request_no=models.ForeignKey(FirModel, on_delete=models.CASCADE)
    request_no=models.OneToOneField(FirModel, on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    father_name=models.CharField(max_length=150)
    dob=models.DateField()
    address=models.TextField()
    nationality=models.CharField(max_length=50)
    relation_with_vicitm=models.CharField(max_length=50)
    occupation=models.CharField(max_length=50)
    doa=models.DateField()
    addhar_no=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)
    crime_pincode=models.IntegerField()
    class Meta:
        db_table="Complainant_Info"

class Fir(models.Model):
    id=models.AutoField(primary_key=True)
    #request_no=models.ForeignKey(FirModel, on_delete=models.CASCADE)
    request_no=models.OneToOneField(FirModel, on_delete=models.CASCADE)
    detail_info=models.TextField()
    class Meta:
        db_table="Fir_Details"

def get_filename(instance, filename):
    old_name = filename
    current_time = datetime.datetime.now().strftime('%Y%m%d%H;%M:%S')
    filename = "%s%s" % (current_time,old_name)
    return os.path.join('images/', filename)

class AttachmentModel(models.Model):
    id=models.AutoField(primary_key=True)
    #request_no=models.ForeignKey(FirModel, on_delete=models.CASCADE)
    sign=models.ImageField(upload_to="img/%y")
    aaddhar_copy=models.ImageField(upload_to="img/%y")
    class Meta:
        db_table="Attachment_doc"

class Suspect(models.Model):
    id=models.AutoField(primary_key=True)
    #request_no=models.ForeignKey(FirModel, on_delete=models.CASCADE)
    request_no=models.OneToOneField(FirModel, on_delete=models.CASCADE)
    other_info=models.TextField()
    class Meta:
        db_table="Suspect_Info"

class Crime(models.Model):
    id=models.AutoField(primary_key=True)
    #request_no=models.ForeignKey(FirModel, on_delete=models.CASCADE)
    request_no=models.OneToOneField(FirModel, on_delete=models.CASCADE)
    poo=models.TextField()
    ooo_from=models.DateTimeField()
    ooo_to=models.DateTimeField()
    city=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    pincode=models.CharField(max_length=20)
    class Meta:
        db_table="Crime_Info"

# Create your models here.
