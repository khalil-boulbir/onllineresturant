from django.urls import path
from .views import VendorRegistration,MyResturant
urlpatterns = [
    path("vendorRegistration",VendorRegistration,name="vendor-registration"),
    path("MyResturant",MyResturant,name="vendor-profile"),

]
