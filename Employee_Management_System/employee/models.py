
from email.mime import image
from django.db import models

# Create your models here.

class Login(models.Model):
    name=models.CharField(max_length=70)
    password=models.CharField(max_length=80)
    email=models.EmailField(max_length=50)
 

class Add(models.Model):
    FirstName=models.CharField(max_length=70)
    MiddelName=models.CharField(max_length=70)
    LastName=models.CharField(max_length=70)
    Password=models.CharField(max_length=70)
    Email=models.EmailField(max_length=70)
    Phone=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    

