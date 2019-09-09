from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'trax_vehicle_manager_data/login.html')

def logout(request):
    return render(request,'trax_vehicle_manager_data/logout.html')

def resetpassword(request):
    return render(request,'trax_vehicle_manager_data/resetpassword.html')

def vehicleslist(request):
    return render(request,'trax_vehicle_manager_data/vehicleslist.html')

def vehicledetail(request):
    return render(request,'trax_vehicle_manager_data/vehicledetail.html')

def vehiclecreate(request):
    return render(request,'trax_vehicle_manager_data/vehiclecreate.html')

def vehicleupdate(request):
    return render(request,'trax_vehicle_manager_data/vehicleupdate.html')

def vehicledelete(request):
    return render(request,'trax_vehicle_manager_data/vehicledelete.html')

def driverslist(request):
    return render(request,'trax_vehicle_manager_data/driverslist.html')

def driverdetail(request):
    return render(request,'trax_vehicle_manager_data/driverdetail.html')

def drivercreate(request):
    return render(request,'trax_vehicle_manager_data/drivercreate.html')

def driverupdate(request):
    return render(request,'trax_vehicle_manager_data/driverupdate.html')

def driverdelete(request):
    return render(request,'trax_vehicle_manager_data/driverdelete.html')

def cleanerslist(request):
    return render(request,'trax_vehicle_manager_data/cleanerslist.html')

def cleanerdetail(request):
    return render(request,'trax_vehicle_manager_data/cleanerdetail.html')

def cleanercreate(request):
    return render(request,'trax_vehicle_manager_data/cleanercreate.html')

def cleanerupdate(request):
    return render(request,'trax_vehicle_manager_data/cleanerupdate.html')

def cleanerdelete(request):
    return render(request,'trax_vehicle_manager_data/cleanerdelete.html')

def customuserlist(request):
    return render(request,'trax_vehicle_manager_data/customuserlist.html')

def customuserdetail(request):
    return render(request,'trax_vehicle_manager_data/customuserdetail.html')

def customusercreate(request):
    return render(request,'trax_vehicle_manager_data/customusercreate.html')

def customuserupdate(request):
    return render(request,'trax_vehicle_manager_data/customuserupdate.html')

def customuserdelete(requset):
    return render(requset,'trax_vehicle_manager_data/customuserdelete.html')

