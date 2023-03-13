from django.forms import ModelForm
from django import forms
from .models import Student,Class,Subject


class StudentForm(ModelForm):   
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'class_name': forms.Select(attrs={'class': 'form-control'}),
        }

class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'subjects':forms.Select(attrs={'class': 'form-control'})
        }


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            "class_name": forms.Select(attrs={'class': 'form-control'})
        }