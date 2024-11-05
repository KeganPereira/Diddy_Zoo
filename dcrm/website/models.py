from django.db import models

from django.contrib.auth.models import AbstractUser 

class ZooUser(AbstractUser): 
    points =models.IntegerField(default=0, blank=True )  
    address= models.CharField(max_length=200, blank=True)
    telephone=models.CharField(max_length=14, blank = True) 


# Create your models here.
