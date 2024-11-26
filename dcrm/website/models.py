from django.db import models

from django.contrib.auth.models import AbstractUser 

from datetime import datetime

class ZooUser(AbstractUser): 
    points =models.IntegerField(default=0, blank=True )  
    address= models.CharField(max_length=200, blank=True)
    telephone=models.CharField(max_length=14, blank = True)  

class enroll1(models.Model):  
    Choices = [ 
        ('4-12','courses age 4-12'), 
        ('13-16','courses age 13-16'), 
        ('17','courses age 17'),
       
    
        ]
    creation_data= models.DateTimeField(auto_now_add = True) 
    courses = models.CharField(max_length=200, choices=Choices) 
    Zoo_ID = models.ForeignKey(ZooUser,on_delete=models.CASCADE) 

class Hotel_Booking(models.Model): 
    booking_id =models.AutoField(primary_key= True, editable= False) 
    hotel_user_id= models.ForeignKey(ZooUser, on_delete= models.CASCADE) 
    hotel_booking_date= models.DateTimeField( blank=True, default=datetime.now) 
    hotel_booking_date_arrive=models.DateField() 
    hotel_booking_date_leave= models.DateField() 
    hotel_booking_adults=models.IntegerField(default = 0)  
    hotel_booking_children=models.IntegerField(default = 0 ) 
    hotel_booking_old_oap=models.IntegerField(default=0) 
    hotel_total_cost=models.FloatField(default = 0) 
    hotel_points=models.IntegerField(default= 0) 

class Zoo_Booking(models.Model): 
    zoo_booking_id= models.AutoField(primary_key=True, editable=False) 
    zoo_user_id= models.ForeignKey(ZooUser, on_delete= models.CASCADE)  
    zoo_booking_date= models.DateTimeField(blank = True, default =datetime.now) 
    zoo_booking_date_arrive=models.DateField() 
    zoo_booking_date_leave=models.DateField() 
    zoo_booking_adults= models.IntegerField(default = 0) 
    zoo_booking_children= models.IntegerField(default = 0) 
    zoo_booking_old_oap=models.IntegerField(default =0) 
    zoo_total_cost= models.FloatField(default = 0 ) 
    zoo_points= models.IntegerField(default = 0)   

class Paymments(models.Model):  
    name_of_card = models.CharField(max_length=200, blank=True)
    card_number= models.CharField(max_length=200) 
    cvv_number = models.CharField(max_length=200) 
    expiry_date= models.CharField(max_length=200)
    


# Create your models here.
