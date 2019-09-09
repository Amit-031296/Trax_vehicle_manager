from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils.managers import InheritanceManager

# Create your models here.

class CustomUser(AbstractUser):
    '''Overrides the custom django user model'''
    # Datafields
    System_administrator = 1
    Boss = 2
    Office_Team = 3
    ROLE_CHOICES = (
        (Office_Team,'Office Team'),
        (Boss,'Boss'),
        (System_administrator,'System administrator')
    )
    user_role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=System_administrator)



class Drivers(models.Model):
        serial_no = models.PositiveSmallIntegerField()
        reference_no = models.IntegerField()
        driver_name = models.CharField(max_length=10)
        vehicle_no = models.IntegerField()
        vehicle_type = models.CharField(max_length=10)
        vehicle_typeofmodule = models.CharField(max_length=10)
        driver_joining_date = models.DateTimeField()
        driver_license_number = models.IntegerField()
        driver_aadhar_number = models.IntegerField()
        driver_contact_number = models.IntegerField()

        def __str__(self):
                return str(self.vehicle_no)
        
        class Meta:
                verbose_name_plural = "Drivers Master List"
                verbose_name = "Driver"

class Cleaners(models.Model):
        cleaner_Id = models.PositiveSmallIntegerField() 
        cleaner_Name = models.CharField(max_length=20)
        cleaner_Age = models.IntegerField()
        cleaner_License_Number = models.IntegerField()
        cleaner_Address = models.CharField(max_length=20)
        cleaner_Contact_Number = models.IntegerField()
        cleaner_Salary = models.IntegerField()

        def __str__(self):
                return str(self.cleaner_Name)
        
        class Meta:
                verbose_name_plural = "Cleaners Master List"
                verbose_name = "Cleaner"

class Vehicles(models.Model):
        vehicle_id = models.PositiveSmallIntegerField()
        vehicle_number = models.IntegerField()
        vehicle_card_number = models.CharField(max_length=10)
        vehicle_seating_capacity = models.IntegerField()
        minimum_average = models.FloatField()
        incremental_average = models.FloatField()
        vehicle_current_status = models.CharField(max_length=10)
        vehicle_buying_date = models.DateTimeField()
        vehicle_type = models.CharField(max_length=10)
        vehicle_ownership = models.CharField(max_length=50)
        vehicle_ownership_details = models.CharField(max_length=20)
        vehicle_manufacturer = models.CharField(max_length=20)

        # Relationship of Vehicle with Drivers and Cleaners
        driver_id = models.ForeignKey(Drivers, on_delete = models.CASCADE)
        cleaner_id = models.ForeignKey(Cleaners, on_delete = models.CASCADE)

        def __str__(self):
            return (self.vehicle_card_number)

        class Meta:
                verbose_name_plural = "Vehicles Master List"
                verbose_name = "Vehicle"

class Expenses(models.Model):
    expense_name = models.CharField(max_length=50)
    expense_id = models.PositiveSmallIntegerField()
    
    
    def __str__(self):
        return str(self.pk)

#Child class of Expenses
class Diesel(Expenses):
    terminal_id = models.PositiveSmallIntegerField()
    transaction_date = models.DateTimeField()
    merchant = models.CharField(max_length=50)
    account_number = models.IntegerField()
    card_used = models.CharField(max_length=50)
    vehicle_number = models.IntegerField()
    vehicle_detail = models.CharField(max_length=50)
    transaction_type = models.CharField(max_length=50)
    diesel_rate = models.IntegerField()
    volume = models.IntegerField()
    amount_Rs = models.PositiveIntegerField()
    balance_Rs = models.PositiveIntegerField()
    odometer_reading = models.PositiveIntegerField()
    ownership = models.CharField(max_length=50)

    def __str__(self):
                return str(self.pk)

#Child class of Expenses
class Maintenance(Expenses):
    YES = 'yes'
    NO = 'no'
    chalak_malak_choices = ((YES,'yes'),(NO,'no'))
    vehicle_number = models.PositiveIntegerField()
    vehicle_detail = models.CharField(max_length=50)
    bill_date = models.DateTimeField()
    vehicle_type = models.CharField(max_length=50)
    chalak_malal = models.CharField(choices=chalak_malak_choices,max_length=100)
    company_name = models.CharField(max_length=50)
    odometer_reading = models.PositiveIntegerField()
    bill_number = models.PositiveIntegerField()
    dealer_part_number = models.PositiveIntegerField()
    particular = models.CharField(max_length=50)
    particular_details = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    rate = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    tax = models.PositiveIntegerField()
    tds = models.PositiveIntegerField()
    labour_charge = models.PositiveIntegerField()	
    total_amount = models.PositiveIntegerField()

    def __str__(self):
                return str(self.pk)

#Child class of Maintenance
class GarageBilling(Maintenance):
    def __str__(self):
                return str(self.pk)

#Child class of Maintenance
class Insurance(Maintenance):
    def __str__(self):
                return str(self.pk)


#Child class of Maintenance
class PoliceSettlements(Maintenance):
    def __str__(self):
                return str(self.pk)

#Child class of Expenses
class RecurringExpenses(Expenses):
    def __str__(self):
                return str(self.pk)

#Child class of RecurringExpenses
class PUC(RecurringExpenses):
    def __str__(self):
                return str(self.pk)

#Child class of RecurringExpenses
class OilChange(RecurringExpenses):
    def __str__(self):
                return str(self.pk)

class Client(models.Model):

    client_name = models.CharField(max_length=200)
    client_address = models.TextField(blank=True)

    def __str__(self):
        return str(self.pk)


