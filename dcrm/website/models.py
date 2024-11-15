from django.db import models

from django.contrib.auth.models import AbstractUser 

class ZooUser(AbstractUser): 
    points =models.IntegerField(default=0, blank=True )  
    address= models.CharField(max_length=200, blank=True)
    telephone=models.CharField(max_length=14, blank = True)  

class enroll1(models.Model):  
    Choices = [ 
        ('4-12','courses age 4-12'), 
        
        #'courses age 12-18',  
        #'courses age 19-20',
    
        ]
    creation_data= models.DateTimeField(auto_now_add = True) 
    courses = models.CharField(max_length=200, choices=Choices) 
    Zoo_ID = models.ForeignKey(ZooUser,on_delete=models.CASCADE) 



# Create your models here.
