from django import forms
from .models import Client, HealthProgram

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
