from asyncio.windows_events import NULL
from email import message
from datetime import date
from django.shortcuts import render, HttpResponse
import string
import random
from numpy import save
from FIR.models import *
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os
from django.contrib import messages
from .form import ImageForm

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
number=0
value=0

# Create your views here.

def generate_random_password():
	## length of password from the user
	length = 8

	## shuffling the characters
	random.shuffle(characters)
	
	## picking random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	## shuffling the resultant password
	random.shuffle(password)

	## converting the list to string
	## printing the list
	return("".join(password))

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'cont.html')

def contact(request):
    return render(request,'cont.html')

# send our email message 'msg' to our boss
def message(subject="Python Notification",
                text=""):
        
     # build message contents
    msg = MIMEMultipart()
        
        # Add Subject
    msg['Subject'] = subject
        
        # Add text contents
    msg.attach(MIMEText(text))

        # Check if we have anything
        # given in the img parameter
    """if img is not None:
            
            # Check whether we have the lists of images or not!
        if type(img) is not list:
                
                # if it isn't a list, make it one
            img = [img]

            # Now iterate through our list
        for one_img in img:
                
                # read the image binary data
            img_data = open(one_img, 'rb').read()
                # Attach the image data to MIMEMultipart
                # using MIMEImage, we add the given filename use os.basename
            msg.attach(MIMEImage(img_data,name=os.path.basename(one_img)))

        # We do the same for
        # attachments as we did for images
        if attachment is not None:
            
            # Check whether we have the
            # lists of attachments or not!
            if type(attachment) is not list:
                
                # if it isn't a list, make it one
                attachment = [attachment]

            for one_attachment in attachment:

                with open(one_attachment, 'rb') as f:
                    
                    # Read in the attachment
                    # using MIMEApplication
                    file = MIMEApplication(f.read(),name=os.path.basename(one_attachment))
                file['Content-Disposition'] = f'attachment;\
                filename="{os.path.basename(one_attachment)}"'
                
                # At last, Add the attachment to our message object
                msg.attach(file)"""
    return msg

def sendemail(stringval="",emailaddress=""):
# initialize connection to our
# email server, we will use gmail here
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()

    # Login with your email and password
    smtp.login('onlinefirsystem81@gmail.com', 'YsvMhatreMirajkar@435')

    # Call the message function
    msg = message("Your response to file FIR was recorded", stringval)

    # Make a list of emails, where you wanna send mail
    to = [emailaddress]

    # Provide some data to the sendmail function!
    smtp.sendmail(from_addr="onlinefirsystem81@gmail.com",
                to_addrs=to, msg=msg.as_string())

    # Finally, don't forget to close the connection
    smtp.quit()

def download_fir(request):
    if request.method=="POST":
        pk= request.POST.get('un')
        password= request.POST.get('pass')
        main_table = FirModel.objects.filter(request_no=pk).values()
        crime_type=main_table[0]['crime_type']
        if crime_type=='1':
            crime_type="child abuse"
        elif crime_type=='0':
            crime_type="Kidnapping"
        else:
            crime_type="Robbery"
        if password == main_table[0]['password']:
            if main_table[0]['fir_status']=="Accepted":
                Complainant_Info = Complainant.objects.filter(request_no=pk).values()
                Fir_Details = Fir.objects.filter(request_no=pk).values()
                Suspect_Info = Suspect.objects.filter(request_no=pk).values()
                Attachment_Doc = AttachmentModel.objects.filter(id=pk).values()
                Crime_Info = Crime.objects.filter(request_no=pk).values()
                police_id= main_table[0]['police_id']
                Full_Name= User.objects.get(id=police_id)
                dict = {
                    "main_table" : main_table[0],
                    "Complainant_Info" : Complainant_Info[0],
                    "Fir_Details" : Fir_Details[0],
                    "Suspect_Info" : Suspect_Info[0],
                    "Attachment_Doc" : Attachment_Doc[0],
                    "Crime_Info" : Crime_Info[0],
                    "pk": pk,
                    "crime_type":crime_type,
                    "Full_Name": Full_Name
                }
                return render(request,'print1.html',dict)
            elif main_table[0]['fir_status']=="pending":
                messages.info(request,'Status still Pending, So FIR cannot be downloaded')
                return render(request,'userlogin.html')
            else:
                messages.info(request,'Status Rejected, you can view status field for more information')
                return render(request,'userlogin.html')
        else:
            messages.info(request,'Invalid Credential')
            return render(request,'userlogin.html')
        
    else:
        return render(request,'userlogin.html')

def track_status(request):
    if request.method=="POST":
        pk= request.POST.get('un')
        password= request.POST.get('pass')
        main_table = FirModel.objects.filter(request_no=pk).values()
        
        if password == main_table[0]['password']:
            dict = {
                    "main_table" : main_table[0],
                }
            return render(request,'track_status.html',dict)
        else:
            messages.info(request,'Invalid Credential')
            return render(request,'userlogin.html')
        
    else:
        return render(request,'userlogin1.html')    


def filefir(request):
    if request.method=="POST":
        value=0
        obj= FirModel.objects.all()
        for val in obj:
            value=val.request_no

        #complaint = Complaint.objects.get(request_no = value)
        #name = complaint.name

        passwordval = generate_random_password()
        saverecard1=FirModel()
        saverecard1.request_no= int(value)+1
        saverecard1.crime_type="1"
        saverecard1.fir_status="pending"
        saverecard1.fir_no=125
        saverecard1.password=passwordval
        print("Hii")
        saverecard1.save()

        saverecard2=Fir()
        saverecard2.request_no_id=int(value)+1
        saverecard2.detail_info=request.POST.get('FIR details')
        print("Hii1")
        saverecard2.save()

        saverecard3=Suspect()
        saverecard3.request_no_id=int(value)+1
        saverecard3.other_info=request.POST.get('Suspect Details')
        print("Hii2")
        saverecard3.save()

        """saverecard4.sign=request.POST.get('sign')
        saverecard4.aaddhar_copy=request.POST.get('aaddhar')"""
        form=ImageForm(data=request.POST,files=request.FILES)
        #form.request_no_id=int(value)+1
        print("Hii3")
        form.save()
        
        saverecard5=Crime()
        saverecard5.request_no_id=int(value)+1
        saverecard5.poo=request.POST.get('poo')
        saverecard5.ooo_from=request.POST.get('date_from')+" "+request.POST.get('time_from')
        saverecard5.ooo_to=request.POST.get('date_to')+" "+request.POST.get('time_to')
        saverecard5.city=request.POST.get('crime_city')
        saverecard5.district=request.POST.get('crime_district')
        saverecard5.state=request.POST.get('crime_state')
        saverecard5.pincode=request.POST.get('crime_Pincode')
        print("Hii4")
        saverecard5.save()
        
        saverecard6=Complainant()
        saverecard6.request_no_id=int(value)+1
        saverecard6.name=request.POST.get('name')
        saverecard6.father_name=request.POST.get('fathername')
        saverecard6.dob=request.POST.get('dob')
        saverecard6.address=request.POST.get('address')
        saverecard6.nationality=request.POST.get('Nationality')
        saverecard6.relation_with_vicitm=request.POST.get('relation')
        saverecard6.occupation=request.POST.get('Occupation')
        saverecard6.doa=date.today()
        saverecard6.addhar_no=request.POST.get('AdhaarNumber')
        saverecard6.email=request.POST.get('Email')
        saverecard6.phone_no=request.POST.get('Phone')
        saverecard6.city=request.POST.get('city')
        saverecard6.district=request.POST.get('district')
        saverecard6.state=request.POST.get('state')
        saverecard6.pincode=request.POST.get('Pincode')
        saverecard6.crime_pincode=request.POST.get('crime_Pincode')
        saverecard6.save()
        print("Hii5")
        stringval = "Hello "+request.POST.get('name')+",\n"+"Be assured our Police Department will revert back to you in 24hrs \nTo check our response login through our system using complaint number= "+str(int(value)+1)+" and password= "+passwordval+"\n Take care, Whole Nation Stands With You"
        sendemail(stringval,request.POST.get('Email'))
        return render(request, 'index.html')

    else:
        form=ImageForm()
        return render(request, 'form.html', {"form":form})

def filefir1(request):
    if request.method=="POST":
        value=0
        obj= FirModel.objects.all()
        for val in obj:
            value=val.request_no

        #complaint = Complaint.objects.get(request_no = value)
        #name = complaint.name

        passwordval = generate_random_password()
        saverecard1=FirModel()
        saverecard1.request_no= int(value)+1
        saverecard1.crime_type="0"
        saverecard1.fir_status="pending"
        saverecard1.fir_no=125
        saverecard1.password=passwordval
        saverecard1.save()

        saverecard2=Fir()
        saverecard2.request_no_id=int(value)+1
        saverecard2.detail_info=request.POST.get('FIR details')
        saverecard2.save()

        saverecard3=Suspect()
        saverecard3.request_no_id=int(value)+1
        saverecard3.other_info=request.POST.get('Suspect Details')
        saverecard3.save()

        """saverecard4.sign=request.POST.get('sign')
        saverecard4.aaddhar_copy=request.POST.get('aaddhar')"""
        form=ImageForm(data=request.POST,files=request.FILES)
        #form.request_no_id=int(value)+1
        form.save()
        
        saverecard5=Crime()
        saverecard5.request_no_id=int(value)+1
        saverecard5.poo=request.POST.get('poo')
        saverecard5.ooo_from=request.POST.get('date_from')+" "+request.POST.get('time_from')
        saverecard5.ooo_to=request.POST.get('date_to')+" "+request.POST.get('time_to')
        saverecard5.city=request.POST.get('crime_city')
        saverecard5.district=request.POST.get('crime_district')
        saverecard5.state=request.POST.get('crime_state')
        saverecard5.pincode=request.POST.get('crime_Pincode')
        saverecard5.save()
        
        saverecard6=Complainant()
        saverecard6.request_no_id=int(value)+1
        saverecard6.name=request.POST.get('name')
        saverecard6.father_name=request.POST.get('fathername')
        saverecard6.dob=request.POST.get('dob')
        saverecard6.address=request.POST.get('address')
        saverecard6.nationality=request.POST.get('Nationality')
        saverecard6.relation_with_vicitm=request.POST.get('relation')
        saverecard6.occupation=request.POST.get('Occupation')
        saverecard6.doa=date.today()
        saverecard6.addhar_no=request.POST.get('AdhaarNumber')
        saverecard6.email=request.POST.get('Email')
        saverecard6.phone_no=request.POST.get('Phone')
        saverecard6.city=request.POST.get('city')
        saverecard6.district=request.POST.get('district')
        saverecard6.state=request.POST.get('state')
        saverecard6.pincode=request.POST.get('Pincode')
        saverecard6.crime_pincode=request.POST.get('crime_Pincode')
        saverecard6.save()
        stringval = "Hello "+request.POST.get('name')+",\n"+"Be assured our Police Department will revert back to you in 24hrs \nTo check our response login through our system using complaint number= "+str(int(value)+1)+" and password= "+passwordval+"\n Take care, Whole Nation Stands With You"
        sendemail(stringval,request.POST.get('Email'))
        return render(request, 'index.html')

    else:
        form=ImageForm()
        return render(request, 'form1.html', {"form":form})

def categories(request):
    return render(request, 'categories.html')



def ngo(request):
    return render(request, 'ngo.html')

def emergency(request):
    return render(request, 'emergency.html')

def quick(request):
    return render(request,'quick.html')