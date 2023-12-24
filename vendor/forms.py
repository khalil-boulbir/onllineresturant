from django import forms
from .models import Vendor
class VendorForm(forms.ModelForm):
    vendor_license = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}))
    vendor_name=forms.CharField(max_length=50)
    class Meta:
        model=Vendor
        fields = ['vendor_name', 'vendor_license']
        