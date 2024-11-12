from django.db import models

from django.contrib.auth.models import AbstractUser 

class ZooUser(AbstractUser): 
    points =models.IntegerField(default=0, blank=True )  
    address= models.CharField(max_length=200, blank=True)
    telephone=models.CharField(max_length=14, blank = True)  

class enroll1(models.Model):  
    
    creation_data= models.DateTimeField(auto_now_add = True) 
    courses = models.CharField(max_length=100) 
    Zoo_ID = models.ForeignKey(ZooUser,on_delete=models.CASCADE) 



# Create your models here.
