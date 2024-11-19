from django.db import models

from django.contrib.auth.models import AbstractUser 

class ZooUser(AbstractUser): 
    points =models.IntegerField(default=0, blank=True )  
    address= models.CharField(max_length=200, blank=True)
    telephone=models.CharField(max_length=14, blank = True)  

class enroll1(models.Model):  
    Choices = [ 
        ('4-12','courses age 4-12'), 
        ('4-12','courses age 4-12'), 
        ('4-12','courses age 4-12'),
       
    
        ]
    creation_data= models.DateTimeField(auto_now_add = True) 
    courses = models.CharField(max_length=200, choices=Choices) 
    Zoo_ID = models.ForeignKey(ZooUser,on_delete=models.CASCADE) 

class Hotel_Booking(models.Model): 
    booking_id =models.AutoField(primary_key= True, editable= False) 
    hotel_user_id= models.ForeignKey(ZooUser, on_delete= models.CASCADE) 
    hotel_booking_date= models.DateField(auto_now_add=True)
    hotel_booking_date_arrive=models.DateField() 
    hotel_booking_date_leave= models.DateField() 
    hotel_booking_adults=models.IntegerField(default = 0)  
    hotel_booking_children=models.IntegerField(default = 0 ) 
    hotel_booking_old_oap=models.IntegerField(default=0) 
    hotel_total_cost=models.FloatField(default = 0) 
    hotel_points=models.IntegerField(default= 0)


# Create your models here.
