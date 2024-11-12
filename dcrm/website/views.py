from django.shortcuts import render , redirect
from  .forms import CreateUserForm, LoginForm ,enroll1_form
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate  
from .models import enroll1
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

@login_required(login_url='my-login')  
def enrolcourses1(request) :
    form= enroll1_form() 
    # if request.method == "POST":  
    #     form=LoginForm(request, data=request.POST) 
    #     if form.is_valid(): 
    #         username=request.POST.get('username') 
    #         password= request.POST.get('password') 
    #         user = authenticate(request, username=username, password=password)  

    #         if user is not None: 
    #             auth.login(request, user) 
    #             return redirect ('') 
    context = {'enroll_form':form}  
    return render(request, 'website/courses1_enrolling.html', context=context)             
                 
                 
             
    






        
