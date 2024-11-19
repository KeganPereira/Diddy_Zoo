from django.urls import path  
from . import views

urlpatterns = [ 
path ('', views.home, name= "") ,
path('register', views.register, name = "register") ,
path('my-login', views.my_login, name = "my-login"), 
path('educational', views.educational, name= "educational"), 
path('courses', views.courses, name= "courses"),
path('courses1', views.courses1, name="courses1") , 
path('logout', views.logout, name= "logout"),
path('enrolcourses1', views.enrolcourses1, name="enrolcourses1"), 
path('courses2', views.courses2, name="courses2"), 
path('map', views.map, name = "map"), 
path('Hotel_Booking', views.Hotel_Booking, name = "Hotel_Booking")

]