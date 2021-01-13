from django.shortcuts import render,redirect
from django.http import HttpResponse
from  app1.models import tbl_user
from  app1.models import tbl_login

# Create your views here.
def index(request): 
    return render(request,'index.html')  
def signin(request): 
    return render(request,'signin.html')  
def register(request):
    if request.method=='POST':
        data=tbl_user()
        data.name=request.POST.get('uname')
        data.email=request.POST.get('uemail')
        data.address=request.POST.get('uaddress')
        data.username=request.POST.get('uusername')
        data.password=request.POST.get('upassword')
        data.country=request.POST.get('ucountry')
        data.save()
        return render(request,'login.html')
    else:
        return HttpResponse("error")    

def login(request):
    if request.method=='POST':
        data=tbl_login()
        data.user_id=request.POST.get('username')
        data.password=request.POST.get('userpassword')
        data.save()
        for da in data:
           if username==da.user_id and password==da.lpassword:
               return render(request,'signin.html')      
    else:
        return HttpResponse("error")    
                  