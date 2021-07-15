from django import forms
from django.forms import fields, widgets
from .models import user

class StudentRegistration(forms.ModelForm):
    class Meta:
        model =user
        fields = ['Name','email','password']
        widgets = {
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }