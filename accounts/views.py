from django.shortcuts import render,redirect

from vendor.models import Vendor
from .models import User,UserProfile
from .forms import UserForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
# Create your views here.

def UserLogin(request):
    if request.user.is_authenticated:
        
        return redirect('myaccount')

    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        print("this email is work",User.objects.get(email=email))
        user=authenticate(email=email,password=password)

        if user is not None:
            user_login=login(request,user)
            return redirect("myaccount")
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect("user-login")
    else:
        return render(request,"login.html")
def myaccount(request):
    user=request.user
    print("user roll",user.role)
    if user.role==2:
        return redirect("customerdashboard")
    elif user.role==1:
         return redirect("vendordashboard")
    else:
        return redirect("admin")
def UserLogout(request):
    logout(request)
    return redirect("user-login") 
def UserSetting(request):
    user=User.objects.get(email=request.user)
    user_profile=UserProfile.objects.get(user=user)
    if user_profile.profile_picture:
        
        context={'form':user,"p_form":user_profile}
    else:
        context={'form':user}
    return render(request,"buyer-account-setting.html",context) 
    
def customerdashboard(request):
    user=User.objects.get(email=request.user)
    
    form=user
    return render(request,"buyer-dashboard.html",{"form":form})
def vendordashboard(request):
    user=User.objects.get(email=request.user)
    form=Vendor.objects.get(user=user)
    
    print(form.vendor_license)
    return render(request,"restaurant-dashboard.html",{"form":form})
def UserRegistration(request):
    
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            user.role=User.COSTUMER
            user.save()
            messages.success(request,"you will be redirect to login page")

            return redirect("user-login")
        else:
            print(forms.errors)
            
    else:
        
        forms=UserForm()
    return render(request,"customer-register.html",{"forms":forms})