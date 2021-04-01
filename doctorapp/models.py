from django.db import models


# Create your models here.

class Admin(models.Model):
    Email=models.EmailField(max_length=25,default="Enter Email",unique=True)
    Password=models.CharField(max_length=25,default="")
    Role=models.CharField(max_length=25,default="")
    Otp=models.IntegerField(max_length=6,default=123456)
    Is_created=models.DateTimeField(auto_now_add=True)
    Is_verified=models.BooleanField(default=False)
    Is_active=models.BooleanField(default=False)



class Doctor(models.Model):
    doctor=models.ForeignKey(Admin,on_delete=models.CASCADE)
    Firstname=models.CharField(max_length=100,default="firstname")
    Lastname=models.CharField(max_length=100,default="lastname")
    Address=models.CharField(max_length=100,default="address")
    Age=models.BigIntegerField(max_length=100,default=10)
    Phonenumber=models.IntegerField(max_length=15,default=5454554)
    Department=models.CharField(max_length=200,default="department")
    # Gender=models.CharField(max_length=30)


class Patient(models.Model):
    patient=models.ForeignKey(Admin,on_delete=models.CASCADE)
    Firstname=models.CharField(max_length=100,default="firstname")
    Lastname=models.CharField(max_length=100,default="lastname")
    Address=models.CharField(max_length=100,default="address")
    Age=models.IntegerField(max_length=12,default=10)
    Phonenumber=models.IntegerField(max_length=12,default=123456789012)
    Gender=models.CharField(max_length=30,default="male")
class Appointment(models.Model):
    docid=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patid=models.ForeignKey(Patient,on_delete=models.CASCADE)
    Gender=models.CharField(max_length=50,default="male")
    Service=models.CharField(max_length=50,default="service")
    Phonnumber=models.IntegerField(max_length=12,default=123456789012)
    Description=models.CharField(max_length=50,default="Description")
    Status=models.CharField(max_length=50,default="Status")




