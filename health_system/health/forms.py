from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Client, HealthProgram, DoctorProfile
from django.db import models
from django.contrib.auth.models import User


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'programs']

        widgets = {
            'programs': forms.CheckboxSelectMultiple(),  
        }
        
class HealthProgramForm(forms.ModelForm):
    class Meta:
        model = HealthProgram
        fields = ['name']

class DoctorLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
       

class DoctorRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    department = forms.CharField(max_length=100, required=True)
    employee_number = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['department', 'employee_number']