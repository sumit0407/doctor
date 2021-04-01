from django.contrib import admin
from django.urls import path,include    
from .import views
urlpatterns = [
    #PAGES URL
    path("",views.Dashboard,name="dashboard"),
    path("Login-page/",views.LoginPage,name="Login"),
    path("Register-page/",views.RegisterPage,name="Registerpage"),
    path("appointment-page/",views.Apointment,name="appointment"),
    path("all-doctors/",views.AllDoctors,name="Alldoctors"),
    path("Profile-page/<int:pk>/",views.Profile,name="ProfilePage"),
    path("Doctor-Admin/",views.DoctorAdmin,name="Doctoradmin"),
    path("Patient-Admin/",views.PatientAdmin,name="Patientadmin"),
    #FUNCTIONALITY URLS
    path("Register-user/",views.Register,name="Register"),
    path("Login-user/",views.LoginUser,name="Loginuser"),
    path("Update-profile-doctor/<int:pk>/",views.UpdateProfileDoctor,name="Updateprofiledoctor")

]