from django.urls import path,include
from .views import (UserRegistration,UserLogin,myaccount,vendordashboard,
                                customerdashboard,UserLogout,UserSetting)

urlpatterns = [
    path("userRegistration",UserRegistration,name="user-registration"),
    path("userLogin",UserLogin,name="user-login"),
    path("UserLogout",UserLogout,name="user-logout"),
    path("UserProfile",UserSetting,name="user-profile"),
    
        path("myaccount",myaccount,name="myaccount"),
    path("myaccount/vendordashboard",vendordashboard,name="vendordashboard"),
    path("myaccount/customerdashboard",customerdashboard,name="customerdashboard"),


    
]
