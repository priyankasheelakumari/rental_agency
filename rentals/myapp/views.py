from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout 
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_agency(request):
    if request.method=='POST':
        username=request.POST['userName']
        password=request.POST['passWord']
        if agency_reg.objects.filter(Uname=username,Password=password).exists():
            var=agency_reg.objects.get(Uname=username)
            if var.approve=='yes':
                u=auth.authenticate(username=username,password=password)
                if u is not None:
                    auth.login(request,u)
                    print("login successfully")
                    return redirect(card_vehicle)
                else:
                    print("INVALID LOGIN")
                    return render(request,'agencylogin.html',{'key':'invalid login'})
            else:
                print('USERNAME NOT FOUND')
                return render(request,'agencylogin.html',{'key':'Only approved user can log'})
        else:
            print("USER NOT FOUND")
            return render(request,'agencylogin.html',{'key':'invalid login'})
    return render(request,'agencylogin.html')   


def reg_agency(request):
    if request.method=='POST':
        Username=request.POST['userName']
        agencynum=request.POST['agencyno']
        name=request.POST['fullname']
        agency_name=request.POST['agencyName']
        email=request.POST['email']
        place=request.POST['place']
        licNo=request.POST['licno']
        mobNo=request.POST['mobno']
        password=request.POST['passWord']
        con_password=request.POST['cpassWord']
        if password==con_password:
            if User.objects.filter(username=Username).exists():
                # user=User.objects.get(username=Username)
                # 
                # if agency_reg.objects.filter(userR=user)
                print("username already exists")
                return render(request,'agencyregistration.html',{'key1':'USERNAME ALREADY EXISTS'})
            elif User.objects.filter(email=email).exists():
                print("email already exists")
                return render(request,'agencyregistration.html',{'key2':'EMAIL ALREADY EXISTS'})
            else:
                user=User.objects.create_user(username=Username,password=password)
                user.save()
                agency=agency_reg(userR=user,Uname=Username,Agencyno=agencynum,Name=name,Aname=agency_name,Email=email,Place=place,Licno=licNo,Mobno=mobNo,Password=password)
                agency.save()
                print("SAVE")
                return redirect(login_agency)
        else:
            return render(request,'agencyregistration.html',{'key3':"PASSWORD DOESNOT MATCH"})
    return render(request,'agencyregistration.html')

            

         

def vehicle(request):
    if request.method=='POST':
        AgencyName=request.user
        rcno=request.POST['rcNo']
        vehno=request.POST['vehNo']
        typeofvehicle=request.POST['type']
        listofvehicles=request.POST['lisT']
        noofseats=request.POST['no-of-seat']
        two_save=veh_details(Agencyname=AgencyName,Rcno=rcno,Vehicleno=vehno,Type_of_vehicle=typeofvehicle,List_of_vehicles=listofvehicles,No_of_seats=noofseats)
        two_save.save()
    return render(request,'vehicle.html')

def card_vehicle(request):
    return render(request,'card.html')
def home(request):
    return render(request,'home.html')
def agency_profile(request):
    username=request.user
    xyz=agency_reg.objects.filter(userR=username).all()
    d={'key':xyz}
    return render(request,'agencyprofile.html',d)
def vehicles_list(request):
    username=request.user
    abc=veh_details.objects.filter(Agencyname=username).all()
    a={'key1':abc}
    return render(request,"vehicle_list.html",a)

def update_list(request,u_id):
    u=veh_details.objects.get(id=u_id)
    if request.method=='POST':
        u.rcno=request.POST['RcNo']
        u.vno=request.POST['VehNo']
        u.typeofveh=request.POST['type']
        u.listofveh=request.POST['lisT']
        u.noofseats=request.POST['seats']
        u.save()
        return redirect(vehicles_list)
    return render(request,'list_update.html',{'updatebtn:u'})


    
         




