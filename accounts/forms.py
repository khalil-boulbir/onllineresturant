from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput)
    repeat_password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if password and repeat_password and password != repeat_password:
            raise forms.ValidationError(
                "Password does not match!"
            )

        return cleaned_data
