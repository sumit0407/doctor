from django.shortcuts import render,redirect
from .models import *
import random
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def Dashboard(request):
    x=Doctor.objects.all()
    return render(request,"app/dashboard/index.html",{"data":x})
def LoginPage(request):
    return render(request,"app/authentication/login.html")
def RegisterPage(request):
    return render(request, "app/authentication/register.html")
def Apointment(request):
    return render(request,"app/appointment/book-appointment.html")
def AllDoctors(request):
    doc=Doctor.objects.all()
    return render(request,"app/doctor/doctors.html",{'doc':doc})
def Profile(request,pk):
    
    pro_id=Doctor.objects.get(id=pk)
    return render(request,"app/doctor/profile.html",{'data':pro_id})
def DoctorAdmin(request):
    return render(request,"app/doctor/doctor-admin.html")
def PatientAdmin(request):
    return render(request,"app/patients/patient-admin.html")
def Register(request):
    role=request.POST['a']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    age=request.POST['age']
    contact=request.POST['contact']
    password=request.POST['password']
    user=Admin.objects.filter(Email=email)
    if role and firstname and lastname and email and age and contact and password:
        if user:
            msg="USER ALLREADY EXISTS"
            return render(request,"app/authentication/register.html",{'err':msg})
        elif role=="Doctor":
            print('IN DOCTOR')
            

            admin_user=Admin.objects.create(Email=email,Password=password,Role=role,Otp=random.randint(10000,99999))
            user=Doctor.objects.create(doctor=admin_user,Firstname=firstname,Lastname=lastname,Age=age,Phonenumber=contact)
            email=request.POST['email']
            msg="Thanks for registration"
            emlist=[]
            emlist.append(email)
            from_email=settings.EMAIL_HOST_USER
            send_mail(emlist,email,msg,from_email)
            return render(request,"app/authentication/login.html")
        elif role=="Patients":
            print('IN Patients')
            admin_user=Admin.objects.create(Email=email,Password=password,Role=role,Otp=random.randint(10000,99999))
            user=Patient.objects.create(patient=admin_user,Firstname=firstname,Lastname=lastname,Age=age,Phonenumber=contact)
            return render(request,"app/authentication/login.html")
    else:
        msg="ALL FIELD ARE REQUIRED"
        return render(request,"app/authentication/register.html",{'err':msg})
        
def LoginUser(request):
    if request.POST['role']=="Doctor":
        email=request.POST['email']
        password=request.POST['password']
        user=Admin.objects.filter(Email=email)
        if len(user)>0:
            if user[0].Password==password and user[0].Role == "Doctor":
                doc=Doctor.objects.get(doctor=user[0])
                request.session['firstname']=doc.Firstname
                request.session['email']=user[0].Email
                request.session['role']=user[0].Role
                request.session['department']=doc.Department
                request.session['id']=user[0].id
                return redirect("Doctoradmin")
            else:
                msg="Password is not match"
                return render(request,"app/authentication/login.html",{'err':msg})
        else:
            msg="user does not exists"
            return render(request,"app/authentication/login.html",{'err':msg})
    
    if request.POST['role'] == "Patients":
        email=request.POST['email']
        password=request.POST['password']
        user1=Admin.objects.filter(Email=email)
        if len(user1)>0:
            if user1[0].Password==password and user1[0].Role == "Patients":
                pat=Patient.objects.get(patient=user1[0])
                request.session['firstname']=pat.Firstname
                request.session['email']=user1[0].Email
                request.session['role']=user1[0].Role
                request.session['phonnumber']=pat.Phonenumber
                request.session['id']=user1[0].id
                return redirect("Patientadmin")
            else:
                msg="Password is not match"
                return render(request,"app/authentication/login.html",{'err':msg})
        else:
            msg="user does not exists"
            return render(request,"app/authentication/login.html",{'err':msg})
    else:
        msg="role not match"
        return render(request,"app/authentication/login.html",{'err':msg}) 
def Updateprofilepages(request,pk):
    ad=Admin.objects.get(id=pk)
    doc=Doctor.objects.get(doctor=ad)


def UpdateProfileDoctor(request,pk):
    ad=Admin.objects.get(id=pk)
    doc=Doctor.objects.get(doctor=ad)
    if request.method == "POST":
        
        doc.Firstname= request.POST['fname'] if request.POST['fname'] else doc.Firstname
        doc.Lastname=request.POST['lname'] if request.POST['lname'] else doc.Lastname
        doc.Address=request.POST['add'] if request.POST['add'] else doc.Address
        doc.Phonenumber=request.POST['phon'] if request.POST['phon'] else doc.Address
        doc.Age=request.POST['age'] if request  .POST['age'] else doc.Age
        doc.Department=request.POST['dep'] if request .POST['dep'] else doc.Department
        
        doc.save()
         
        url=f"/Profile-page/{pk}/"
        return redirect(url)

        
      

        
        


           
        
    


    








            
    