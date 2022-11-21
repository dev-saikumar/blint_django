from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Outlets,Products,Orders
from django.contrib.auth import authenticate,logout as user_logout,login as user_login
# Create your views here.


def login(req):
    if(req.user.is_authenticated):
        return redirect('homepage')
    
    if(req.method=='POST'):
        print(req.POST.get('email'))
        print(req.POST.get('pass'))
        user_auth=authenticate(password=req.POST.get('pass'),username=req.POST.get('username'))
        user_login(req,user_auth)
        return render(req,'home.html')
    else:
        return render(req,'login.html')
def logout(req):
    user_logout(req)
    return redirect('homepage')

def register(req):

    if(req.user.is_authenticated):
        return redirect('homepage')
    print("---------------------------------------------------------")
    if(req.method=='POST'):
        fname=req.POST.get('fname')
        lname=req.POST.get('lname')
        email=req.POST.get('email')
        username=req.POST.get('username')
        pswd=req.POST.get('pswd')
        User.objects.create_user(username=username,email=email,password=pswd,first_name=fname,last_name=lname)
        User.save(req)
        return render(req,'login.html')
    else:
        return render(req,'register.html')

def homepage(req):

    if(req.user.is_authenticated):
        if(User.is_staff):
            return redirect('vendor_homepage')
        
        
        return render(req,'home.html')
    else:
        return redirect('login')

def vendor_homepage(req):
    return render(req,'vendor_homepage.html')
def home(request):
    return render(request,'home.html')