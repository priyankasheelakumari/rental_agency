from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class agency_reg(models.Model):
    userR=models.ForeignKey(User,on_delete=models.CASCADE)
    Agencyno=models.IntegerField(primary_key=True)
    Uname=models.CharField(max_length=50,null=True)
    Name=models.CharField(max_length=30,null=True)
    Aname=models.CharField(max_length=50,null=True)
    Email=models.EmailField(null=True)
    Place=models.CharField(max_length=50,null=True)
    Licno=models.IntegerField(null=True)
    Mobno=models.IntegerField(null=True)
    Password=models.CharField(max_length=30,null=True)
    approve=models.CharField(max_length=30,null=True,default="no")

class veh_details(models.Model):
    Agencyname=models.CharField(max_length=30,null=True)
    Rcno=models.IntegerField(null=True)
    Vehicleno=models.CharField(null=True,max_length=10)
    Type_of_vehicle=models.CharField(max_length=50,null=True)
    List_of_vehicles=models.CharField(max_length=30,null=True)
    No_of_seats=models.IntegerField(null=True)
    approve=models.CharField(max_length=30,null=True,default="no")


