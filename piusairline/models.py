from django.db import models
from django.db.models import manager
from django.contrib.auth.models import User, AbstractUser
from datetime import datetime, timedelta

# DB Tables tobe created by models
# Tickets Tables, booking, users(staff & Customers)[use Dhango authTable], 
class Tickets(models.Model):
    ticketName = models.CharField(max_length=100)# Name of Airplane
    ticketType = models.CharField(max_length=100) #The Class of ticket Economy, First
    status = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False) #Is tickect available or sold
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateSold = models.DateTimeField(null=True)
    buyerID = models.IntegerField(null=True)
    ticketAuthor = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    departureDate = models.DateTimeField(default=datetime.now()+timedelta(days=29))
    destinationCountry = models.CharField(max_length=150, null=True) #Airports codes OR State and country 
    destinationState = models.CharField(max_length=150, null=True)
    destinationAirport = models.CharField(max_length=150, null=True)
    departureCountry = models.CharField(max_length=150, null=True) 
    departureState = models.CharField(max_length=150, null=True)
    departureAirport = models.CharField(max_length=150, null=True)
    arrivalDate = models.DateTimeField(default=datetime.now()+timedelta(days=30))

    

# Model for purchase / Sales of tickets 
class Sales(models.Model):
    buyerID = models.IntegerField()#Customer user ID
    # staffID = models.IntegerField() #Piusairline Sales Representative's user ID
    ticketID = models.IntegerField()
    # amount === Already in the Ticket Table
    dateSold = models.DateTimeField(auto_now_add=True)
    # salesLocation = models.TextField() # Sales agent Location
    paymentType = models.TextField() #Payment method cash, POS, Cheque, Transfer etc
    # flightName = models.TextField()

class Usersdetails(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
   country = models.CharField(max_length=150)
   state = models.CharField(max_length=150)
   phone = models.CharField(max_length=256, blank=True, null=True)
   gender = models.CharField(max_length=10)
    # email = models.EmailField()
    # userid = models.CharField(max_length = 100)
    # country = models.TextField()
    # state = models.TextField()
    # regdate = models.DateTimeField(auto_now_add=True)
    # status = models.IntegerField()
    # description = models.TextField()
    # special = models.TextField()