from django.urls import path  
from . import views

urlpatterns = [ 
path ('', views.home, name= "") ,
path('register', views.register, name = "register") ,
path('my-login', views.my_login, name = "my-login"), 
path('educational', views.educational, name= "educational"), 
path('courses', views.courses, name= "courses")


]