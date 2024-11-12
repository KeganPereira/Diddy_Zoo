from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User 
from .models import ZooUser, enroll1

from django import forms 
from django.forms.widgets import PasswordInput, TextInput 

#- register or create user 
class CreateUserForm(UserCreationForm): 
    class Meta:  
        model = ZooUser
        fields= ['username', 'password1', 'password2' ,'first_name', 'last_name','email','address','telephone']  

        #- Login User 

class LoginForm(AuthenticationForm): 
    username =forms.CharField(widget= TextInput()) 
    password= forms.CharField(widget= PasswordInput())   

class enroll1_form():
    class Meta: 
        model =  enroll1  
        fields = ['courses']
