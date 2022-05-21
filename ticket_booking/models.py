import email
from django.db import models

# Create your models here.
class RequistOtpAuth(models.Model):
    username = models.CharField(max_length=50,default='')
    otp = models.IntegerField(default=0) 
    

    def __str__(self) -> str:
        return self.username

class BookSeat(models.Model):
    username = models.CharField(max_length=50,default='')
    userEmail = models.CharField(max_length=50,default='')
    whereTo = models.CharField(max_length=50,default='')
    howMany = models.CharField(max_length=50,default='')
    arrivals = models.CharField(max_length=50,default='')
    leaving = models.CharField(max_length=50,default='')

    def __str__(self) -> str:
        return self.username
    
class UserSavedMessages(models.Model):
    name = models.CharField(max_length=50,default='')
    email = models.CharField(max_length=50,default='')
    number = models.CharField(max_length=50,default='')
    subject = models.CharField(max_length=50,default='')
    message =  models.CharField(max_length=500,default='')

    def __str__(self) -> str:
        return self.name
    