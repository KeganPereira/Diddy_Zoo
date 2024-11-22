from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User 
from .models import ZooUser, enroll1,Hotel_Booking

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

class enroll1_form(forms.ModelForm):
    class Meta: 
        model =  enroll1  
        fields = ['courses']
        widgets= { 
            'courses': forms.Select(choices=enroll1.Choices)
        } 

class Hotel_Booking_Form(forms.ModelForm): 
    class Meta: 
        model = Hotel_Booking 
        fields= ['hotel_booking_date_arrive', 'hotel_booking_date_leave', 'hotel_booking_adults', 
                 'hotel_booking_old_oap', 'hotel_booking_children', "hotel_total_cost", 'hotel_points' ] 
        labels = { 
             "hotel_booking_date_arrive": "day you wish to arrive", 

        }  
        widgets = { 
              'hotel_booking_date_arrive': forms.DateInput(attrs={'type': 'date'}), 
              'hotel_booking_date_leave': forms.DateInput(attrs={'type': 'date'}),   
              'hotel_total_cost':forms.HiddenInput(), 
              'hotel_points': forms.HiddenInput(), 



        } 

    def  __init__(self, *args,**kwargs): 
        super().__init__(*args, **kwargs)


# class profile_form(forms.ModelForm): 
#     class Meta:  
#         model = ZooUser
#         fields= ['username', 'password1', 'password2' ,'first_name', 'last_name','email','address','telephone', 'points']  

 
