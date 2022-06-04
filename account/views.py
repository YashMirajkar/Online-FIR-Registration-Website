from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from matplotlib.style import use
from FIR.models import *
from ofs import settings
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        pincode = request.POST['pincode']
        email = request.POST['email']
        station = request.POST['station']
        if(password1==password2):
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
                user.save()
                """users = User.objects.get(username=username)
                users.pincode = pincode
                users.Police_Station = station
                users.save()"""
                messages.info(request,'User Created')
                return redirect('login')

        else: 
            messages.info(request,'Password Not Matching')
        return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        #return render(request,'home.html', {"UN":username})
        if user is not None:
            auth.login(request, user)
            messages.info(request,'Login Successful')
            return render(request,'home.html', {"username":username})
            #redirect('home')
        else:
            messages.info(request,'invalid credenials')
            return render(request,'login_form.html')
        

    else:
        return render(request,'login_form.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def viewfir(request,username):
    obj= Complainant.objects.select_related('request_no')
    obj1=User.objects.filter(username=username).values('id')
    id=obj1[0]['id']
    pincode=Police_Info.objects.filter(user_id=id).values('pincode')

    print(pincode[0]['pincode'])
    # #obj1 = Complainant.objects.filter(obj.request_no).get('doa')
    # print(obj.query)
    # #a = Complainant.objects.select_related('request_no')
    """firs = FirModel.objects.all()
    complainants = []
    crime_types = []
    for i in firs:
        complainant = Complainant.objects.get(request_no_id = i.request_no)
        # print(complainant.query)
        # complainants.append(complainant)
        # crime_types.append(i.crime_type)
        print(complainant)
        print(i.request_no)
    print(complainants)
    print(crime_types)"""
    dict={
        "obj":obj,
        "username":username,
        "pincode":pincode[0]['pincode']
    }
    return render(request,'viewfir.html',dict)

def home(request,username):
    dict={
        "username":username
    }
    return render(request,'home.html',dict)

def profile(request,username):
    obj= User.objects.filter(username=username).values()
    obj1= Police_Info.objects.filter(user_id=obj[0]['id'])
    dict={
        "obj":obj[0],
        "obj1":obj1[0],
        "username":username
    }
    return render(request,'profile.html',dict)

def loadfir(request,pk,username):
    #Complainant_no = request.POST.get('Complainant_no.')
    main_table = FirModel.objects.filter(request_no=pk).values()
    Complainant_Info = Complainant.objects.filter(request_no=pk).values()
    Fir_Details = Fir.objects.filter(request_no=pk).values()
    Attachment_Doc = AttachmentModel.objects.filter(id=pk).values()
    Suspect_Info = Suspect.objects.filter(request_no=pk).values()
    Crime_Info = Crime.objects.filter(request_no=pk).values()
    crime_type=main_table[0]['crime_type']
    if crime_type=='1':
        crime_type="child abuse"
    elif crime_type=='0':
        crime_type="Kidnapping"
    else:
        crime_type="Robbery"
    dict = {
        "main_table" : main_table[0],
        "Complainant_Info" : Complainant_Info[0],
        "Fir_Details" : Fir_Details[0],
        "Attachment_Doc" : Attachment_Doc[0],
        "Suspect_Info" : Suspect_Info[0],
        "Crime_Info" : Crime_Info[0],
        'media_url':settings.MEDIA_URL,
        'crime_type':crime_type,
        'pk': pk,
        "username": username
    }
    #return render(request,'police_form.html',{"dict":obj})
    #print(Attachment_Doc[0].aaddhar_copy)
    return render(request,'fir_display.html',dict)

def printfir(request,pk,username):
    main_table = FirModel.objects.filter(request_no=pk).values()
    Complainant_Info = Complainant.objects.filter(request_no=pk).values()
    Fir_Details = Fir.objects.filter(request_no=pk).values()
    Suspect_Info = Suspect.objects.filter(request_no=pk).values()
    Attachment_Doc = AttachmentModel.objects.filter(id=pk).values()
    Crime_Info = Crime.objects.filter(request_no=pk).values()
    Full_Name= User.objects.get(username=username)
    crime_type=main_table[0]['crime_type']
    if crime_type=='1':
        crime_type="child abuse"
    elif crime_type=='0':
        crime_type="Kidnapping"
    else:
        crime_type="Robbery"
    dict = {
        "main_table" : main_table[0],
        "Complainant_Info" : Complainant_Info[0],
        "Fir_Details" : Fir_Details[0],
        "Suspect_Info" : Suspect_Info[0],
        "Attachment_Doc" : Attachment_Doc[0],
        "Crime_Info" : Crime_Info[0],
        'media_url':settings.MEDIA_URL,
        "pk": pk,
        "username": username,
        "Full_Name": Full_Name,
        "crime_type": crime_type
    }
    return render(request,'print.html',dict)

def updatestatus(request,pk,username):
    if request.method=='POST':
        obj1=User.objects.filter(username=username).values('id')
        id=obj1[0]['id']
        if request.POST.get('status')=="Accepted":
            main_table= FirModel.objects.get(request_no=pk)
            main_table.fir_no= request.POST.get('fir_number')
            main_table.fir_status= "Accepted"
            main_table.police_id= id
            main_table.save()
            dict= {
                "pk":pk,
                "username":username
            }
            return render(request,'Ustatus.html', dict)
        elif request.POST.get('status')=="Rejected":
            main_table= FirModel.objects.get(request_no=pk)
            main_table.fir_status= "Rejected"
            main_table.comments= request.POST.get('comment')
            main_table.police_id= id
            main_table.save()
        return render(request,'home.html',{"username":username})

    else:
        dict= {
                "pk":pk,
                "username":username
        }
        return render(request,'Ustatus.html', dict)
    

def contact(request,pk,username):
    Complainant_Info = Complainant.objects.filter(request_no=pk).values()
    dict = {
        "Complainant_Info":Complainant_Info[0],
        "username":username
    }
    return render(request,'Contact.html',dict)