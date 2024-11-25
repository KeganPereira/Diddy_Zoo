from django.shortcuts import render , redirect
from  .forms import CreateUserForm, LoginForm ,enroll1_form ,Hotel_Booking_Form,Zoo_Booking_Form
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate  
from .models import enroll1, Hotel_Booking
from django.contrib.auth.decorators import login_required

# Create your views here.  

from django.http import HttpResponse 

def home(request): 
    return render(request, 'website/index.html')  
def register(request):  

    form= CreateUserForm() 
    if request.method == "POST": 
        form = CreateUserForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('my-login') 
    context = {'form': form}

    return render(request, 'website/register.html', context= context ) 

def my_login(request): 
    form= LoginForm() 
    if request.method == "POST":  
        form=LoginForm(request, data=request.POST) 
        if form.is_valid(): 
            username=request.POST.get('username') 
            password= request.POST.get('password') 
            user = authenticate(request, username=username, password=password)  

            if user is not None: 
                auth.login(request, user) 
                return redirect ('') 
    context = {'login_form':form}  
    return render(request, 'website/my-login.html', context=context)   

def logout(request): 
    auth.logout(request)  
    return redirect('my-login')


def educational(request): 
    return render(request, 'website/educational-tours.html')  

def courses(request): 
    return render(request, 'website/educational_courses.html') 

def courses1(request): 
    return render(request, 'website/courses1.html')   

def courses2(request): 
    return render (request,'website/courses2.html' )   

def courses3(request): 
    return render (request, 'website/courses3.html')
def map (request): 
    return render (request, 'website/map.html') 



    #-------------------------------------------------------------------------------------------------------------------#

@login_required(login_url='my-login')  
def enrolcourses1(request) :
    form= enroll1_form() 

    if request.method == "POST":  
       updated_request = request.POST.copy() 
       updated_request.update({'Zoo_ID_id': request.user}) 

       form = enroll1_form(updated_request) 

       if form.is_valid(): 

            obj = form.save(commit=False)
            obj.Zoo_ID_id = request.user.id
            obj.save()

            return redirect ('') 
       else:
            print("Form is not valid")

    context = {'enroll_form':form}  
    return render(request, 'website/courses1_enrolling.html', context=context)      

@login_required(login_url='my-login') 
def Hotel_Booking(request):  

    form = Hotel_Booking_Form() 

    if request.method == "POST":  
        updated_request=request.POST.copy() 
        updated_request.update({'hotel_user_id_id': request.user}) 

        form = Hotel_Booking_Form(updated_request) 

        if form.is_valid(): 
            obj1= form.save(commit=False) 


            arrive= obj1.hotel_booking_date_arrive 
            depart =obj1.hotel_booking_date_leave 
            result = depart -arrive  
            print("Number of days: ",  result.days) 

            hotel_total_cost = int(obj1.hotel_booking_adults)*65 \
                            + int(obj1.hotel_booking_children)* 35\
                            +int(obj1.hotel_booking_old_oap)*40  
            
            hotel_total_cost*= int(result.days) 

            hotel_points=int(hotel_total_cost/20) 
            print("Hotel Points: ", hotel_points) 
            print("Printing booking costs: " ,  hotel_total_cost)  

            obj1.hotel_points = hotel_points
            obj1.hotel_total_cost= hotel_total_cost 
            obj1.hotel_user_id= request.user 


            obj1.save() 

            return redirect('') 
        else: 
            print('There was a problem with the form') 
            return redirect ('')
        
    context = {'form':form}   
    return render(request,'website/hotel.html', context=context)  

@login_required(login_url='my-login') 
def Ticket_Booking(request):   
    form = Zoo_Booking_Form() 

    if request.method== "POST": 
        updated_request=request.POST.copy() 
        updated_request.update = ({"zoo_user_id_id": request.user})  

        form= Zoo_Booking_Form(updated_request) 
        if form.is_valid(): 
            obj1= form.save(commit=False)   


            arrive= obj1.zoo_booking_date_arrive 
            depart =obj1.zoo_booking_date_leave 
            result = depart - arrive  
            print("Number of days: ",  result.days)  

            zoo_total_cost = int(obj1.zoo_booking_adults)*65 \
                             +int(obj1.zoo_booking_children)* 35 \
                             +int(obj1.zoo_booking_old_oap)*40  
            zoo_total_cost*= int(result.days) 

            zoo_points= int(zoo_total_cost/20)  
            print("Zoo Points: ", zoo_points) 
            print("Printing booking costs: " ,  zoo_total_cost)   
            obj1.zoo_points = zoo_points
            obj1.zoo_total_cost= zoo_total_cost 
            obj1.zoo_user_id= request.user  
            obj1.save() 

            return redirect('') 
        else: 
            print('There was a problem with the form') 
            return redirect ('')
        
    context = {'Ticket_Form':form}   
    return render(request,'website/zoo_booking.html', context=context)    


@login_required(login_url='my-login')  
def Payments(request)   
    one_record = ZooUser.objects.get(id=request.user.id) 
    booking = ModelBooking.objects.latest("hotel_user_id")
    form =  Payments_Form()  
     if requests_method == "POST" 
          
        updated_request=request.POST.copy() 
        updated_request.update = ({"Hotel_user_id_id": request.user})  

        form= Payments_Form(updated_request,self) 
        if form.is_valid(): 
            obj1= form.save(commit=False)   











         



        

   
                 
             
    






        
