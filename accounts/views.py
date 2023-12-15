from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def UserLogin(request):
    pass
def UserRegistration(request):
    
    if request.method=="POST":
        forms=UserForm(request.POST)
        if forms.is_valid():
            # Save the user instance to the database
            user = forms.save(commit=False)
            user.role=User.COSTUMER
            user.save()
            email=forms.cleaned_data.get("email")
            password=forms.cleaned_data.get("paswword1")
            print(f'email is {email} and password is {password}')
            user = authenticate(request, username=email, password=password)
            login(request, user)
            print("77777")
            messages.success(request, 'Registration successful. You are now logged in.')

            return redirect("user-registration")
        else:
            print(forms.errors)
            
    else:
        
        forms=UserForm()
    return render(request,"register-restaurant.html",{"forms":forms})