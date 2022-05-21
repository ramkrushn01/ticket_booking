from django import views
from django.urls import path
from ticket_booking import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sendotp', views.sendOtp, name='sendotp'),
    path('singup',views.signUpUser,name='singup'),
    path('login',views.loginUser,name='userlogin'),
    path('logout',views.logoutUser,name='userlogin'),
    path('test',views.test,name='test'),
    path('book',views.bookNow,name='book'),
    path('myallbooking',views.myAllBooking,name='myallbooking'),
    path('sendmsg',views.saveUserMessage,name='sendmsg')

    
]
