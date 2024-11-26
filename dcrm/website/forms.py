from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User 
from .models import ZooUser, enroll1,Hotel_Booking, Zoo_Booking,Paymments

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


class Zoo_Booking_Form(forms.ModelForm): 
      class Meta: 
        model = Zoo_Booking  
        fields = ['zoo_booking_date_arrive', 'zoo_booking_date_leave', 'zoo_booking_adults', 
        'zoo_booking_old_oap', 'zoo_booking_children', 'zoo_total_cost', 'zoo_points'] 
        labels= { 
            "zoo_booking_date_arrive": "day you wish to arrive", 

        } 
        widgets = { 
              'zoo_booking_date_arrive': forms.DateInput(attrs={'type': 'date'}), 
              'zoo_booking_date_leave': forms.DateInput(attrs={'type': 'date'}),   
              'zoo_total_cost':forms.HiddenInput(), 
              'zoo_points': forms.HiddenInput(), 

        } 
        def __init__(self, *args, **kwargs): 
         super().__init__(*args, **kwargs) 



class Payments_Form(forms. ModelForm): 
       class Meta: 
        model= Paymments 
        fields = ['name_of_card', 'card_number', 'cvv_number', 'expiry_date' ] 
        labels= { 
             "card_number":"Enter your card number",  
             "name_of_card": "Enter card name", 
             "cvv_number": "Please enter your cvv number", 
             "expiry_date":"Please enter your expiry date" 
        


        } 

        # # widgets ={   
        # #     { 
        # #         "name_of_card": forms.CharField(attrs={"placeholder": "Name of Card"}), 

        # #     }


               
        


        # }

# # class profile_form(forms.ModelForm): 
#     class Meta:  
#         model = ZooUser
#         fields= ['username', 'password1', 'password2' ,'first_name', 'last_name','email','address','telephone', 'points']  

 
