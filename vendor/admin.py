from django.contrib import admin
from .models import Vendor
# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display=['vendor_name', 'vendor_license']
admin.site.register(Vendor,VendorAdmin)