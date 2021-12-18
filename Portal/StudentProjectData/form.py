from django import forms
from django.forms.widgets import TextInput
from .models import StudentProjectModel

class StudentProjectForm(forms.ModelForm):
    class Meta:
        model = StudentProjectModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'True','autocomplete':"off"}),
            'studentId': forms.TextInput(attrs={'class': 'form-control', 'required': 'True','autocomplete':"off"}),
            'projectChoose' : forms.Select(attrs={'class':'form-control','required':'True','autocomplete':"off"})
        }
        labels = {
            'name': 'Student Name:',
            'studentId': 'Student Id:',
            'projectChoose' : 'Mini Project Topics'
        }