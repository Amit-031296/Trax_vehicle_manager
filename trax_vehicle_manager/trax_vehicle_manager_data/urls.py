from django.contrib import admin
from django.urls import path
from trax_vehicle_manager_data import views

app_name='trax_vehicle_manager_data'

urlpatterns = [
    #Here We Post The Views For Our Application

    #url for login page
    path('',views.login,name='Login'),
    
    #url for logout page
    path('logout/',views.logout,name='Logout'),

    #url for reset password page
    
    path('resetpassword/',views.resetpassword,name='Resetpassword'),
    
    #url for vehicle list page
    path('vehicleslist/',views.vehicleslist,name='vehicleslist'),
    
    #url for vehicle detail page
    path('vehicledetails/',views.vehicledetail,name='vehicledetails'),
    
    #url for vehicle create page
    path('vehiclecreate/',views.vehiclecreate,name='vehiclecreate'),
    
    #url for vehicle update page
    path('vehicleupdate/',views.vehicleupdate,name='vehicleupdate'),
    
    #url for vehicle delete page
    path('vehicledelete/',views.vehicledelete,name='vehicledelete'),
    
    #url for driver list page
    path('driverslist/',views.driverslist,name='driverslist'),
    
    #url for driver details page
    path('driverdetails/',views.driverdetail,name='driverdetails'),
    
    #url for driver create page
    path('drivercreate/',views.drivercreate,name='drivercreate'),
    
    #url for driver update page
    path('driverupdate/',views.driverupdate,name='driverupdate'),
    
    #url for driver delete page
    path('driverdelete/',views.driverdelete,name='driverdelete'),
    
    #url for cleaners list page
    path('cleanerslist/',views.cleanerslist,name='cleanerslist'),
    
    #url for cleaner details page
    path('cleanerdetails/',views.cleanerdetail,name='cleanerdetails'),
    
    #url for cleaner create page
    path('cleanercreate/',views.cleanercreate,name='cleanercreate'),
    
    #url for cleaner update page
    path('cleanerupdate/',views.cleanerupdate,name='cleanerupdate'),
    
    #url for cleaner delete page
    path('cleanerdelete/',views.cleanerdelete,name='cleanerdelete'),
    
    #url for customusers list page
    path('customuserslist/',views.customuserlist,name='customuserslist'),
    
    #url for customuser details page
    path('customuserdetails/',views.customuserdetail,name='customuserdetails'),
    
    #url for customuser create page
    path('customusercreate/',views.customusercreate,name='customusercreate'),
    
    #url for customuser update page
    path('customuserupdate/',views.customuserupdate,name='customuserupdate'),
    
    #url for customuser delete page
    path('customuserdelete/',views.customuserdelete,name='customuserdelete'),    
]
