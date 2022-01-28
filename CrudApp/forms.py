from django import forms
from django.forms import widgets
from django.forms.models import ModelForm
from .models import Student

class AddStudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=("name","rollno","city")
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'rollno':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'})
        }