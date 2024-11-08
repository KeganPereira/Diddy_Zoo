from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User 
from .models import ZooUser

from django import forms 
from django.forms.widgets import PasswordInput, TextInput 

#- register or create user 
class CreateUserForm(UserCreationForm): 
    class Meta:  
        model = ZooUser
        fields= ['username', 'password', 'password2', 'first_name', 'last_name','email','address','telephone']  

        #- Login User 

class LoginForm(AuthenticationForm): 
    username =forms.CharField(widget= TextInput()) 
    password= forms.CharField(widget= PasswordInput())  
