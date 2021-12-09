from django import forms
from .models import StudentRegistration


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'True','autocomplete':"off"}),
            'studentId': forms.TextInput(attrs={'class': 'form-control', 'required': 'True','autocomplete':"off"}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'required': 'True','autocomplete':"off"}),
            'gender' : forms.Select(attrs={'class': 'form-control', 'required': 'True','autocomplete':"off"}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'required': 'True', 'type':'date','autocomplete':"off"}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'required': 'True','autocomplete':"off"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'True','autocomplete':"off"}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'required': 'True','autocomplete':"off"}),
            'semester': forms.Select(attrs={'class': 'form-control', 'required': 'True','autocomplete':"off"}),
            'yearOfAdmission': forms.DateInput(attrs={'class': 'form-control', 'required':'True', 'type':'date','autocomplete':"off"}),
            'yearOfPassout': forms.DateInput(attrs={'class': 'form-control', 'required': 'True', 'type':'date','autocomplete':"off"}),
        }
        labels = {
            'name': 'Student Name:',
            'studentId': 'Student Id:',
            'password': 'Set Password:',
            'gender' : 'Gender',
            'date_of_birth': 'Date Of Birth:',
            'phone_number': 'Student Mobile Number:',
            'email': 'Student Email:',
            'course': 'Course:',
            'semester':'Semester',
            'yearOfAdmission': 'Year Of Admission',
            'yearOfPassout': 'Year Of Pass Out'
        }