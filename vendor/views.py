from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from accounts.models import User,UserProfile
from accounts.forms import UserForm
from .forms import VendorForm
from .models import Vendor
import time

def VendorRegistration(request):
    
    if request.method == "POST":
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST, request.FILES)
        if form.is_valid() and v_form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            user.role = User.VENDOR
            user.save()
            print(v_form.cleaned_data)
            vendor_license=v_form.cleaned_data.get("vendor_license")
            vendor_name=form.cleaned_data.get("vendor_name")
            vendor = v_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            
            return redirect("user-login")
        else:
            print(form.errors)
            print(v_form.errors)
    else:
        form = UserForm()
        v_form = VendorForm()
    
    return render(request, "vendor-register.html", {"form": form, "v_form": v_form})
def MyResturant(request):
    user=User.objects.get(email=request.user)
    form=Vendor.objects.get(user=user)
    return render(request,"restaurant-restaurant.html",{"form":form})