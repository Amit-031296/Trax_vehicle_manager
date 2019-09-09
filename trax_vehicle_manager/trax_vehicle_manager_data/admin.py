from django.contrib import admin
from trax_vehicle_manager_data.models import Drivers,Cleaners,Vehicles,Expenses,Diesel,Maintenance,GarageBilling,CustomUser,Insurance,Client,PoliceSettlements,RecurringExpenses,OilChange,PUC

# Register your models here.

admin.site.register(Drivers)
admin.site.register(Cleaners)
admin.site.register(Vehicles)
admin.site.register(Expenses)
admin.site.register(Diesel)
admin.site.register(Maintenance)
admin.site.register(GarageBilling)
admin.site.register(CustomUser)
admin.site.register(Insurance)
admin.site.register(Client)
admin.site.register(PoliceSettlements)
admin.site.register(RecurringExpenses)
admin.site.register(OilChange)
admin.site.register(PUC)
