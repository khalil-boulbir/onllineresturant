from django.urls import path,include
from .views import UserRegistration,UserLogin

urlpatterns = [
    path("userRegistration",UserRegistration,name="user-registration"),
    path("userLogin",UserLogin,name="user-login"),

    
]
